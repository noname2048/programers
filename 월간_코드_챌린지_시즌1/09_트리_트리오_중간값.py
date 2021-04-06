from collections import defaultdict, deque
from typing import DefaultDict, List
from time import time

def tester_maker(solution):
    """주어진 함수에 대해 테스트케이스 셋을 넣어 함수를 다시 만든다
    a = tester_maker(solution)
    a() => 작동
    """

    n_list = [
        4,
        5,
        6,
        7,
        16,
        14,
        14
    ]

    edges_list = [
        [[1, 2], [2, 3], [3, 4]],
        [[1, 5], [2, 5], [3, 5], [4, 5]],
        [[1, 6], [2, 3], [3, 5], [3, 4], [2, 6]],
        [[1, 2], [2, 3], [1, 4], [1, 5], [5, 7], [5, 6]],
        [[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[2, 11],[11, 13],
            [11, 12],[3, 14],[4, 15],[15, 16],[5, 9],[9, 10],],
        [[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[8, 9],[5, 11],[11, 12],[6, 13],[13, 14],],
        [[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[8, 9],[4, 11],[11, 12],[5, 13],[13, 14],],
    ]

    ans_list = [
        2,
        2,
        4,
        4,
        8,
        7,
        7,
    ]

    def wrapper():
        
        for i, n in enumerate(n_list):
            print(f"#{i + 1:03d}", end="")
            st = time()
            ret = solution(n, edges_list[i])
            run_time = time() - st
            print(f"({int(run_time * 1000)}ms) ret: [{ret}] ans: {ans_list[i]}")

    return wrapper


def get_farthest_point_from_point_with_path(start, adj, path=False):
    """start point와 adj: List[set]를 통해 dfs로 가장 먼곳을 찾는 함수
    path가 true이면 start부터 찾은 점까지의 경로를 반환한다

    리턴값은
    1. where 해당 노드의 번호
    2. 해당 노드까지의 길이
    3. 경로
    """
    global_depth = local_depth = 0
    where = here = start

    visited = defaultdict(int)
    visited[here] = here

    stack = deque()
    stack.append([here, local_depth])

    while len(stack):
        here, local_depth = stack.pop()

        for child in adj[here]:
            if visited[child] == 0:
                visited[child] = here
                stack.append([child, local_depth + 1])

                if global_depth < local_depth + 1:
                    global_depth = local_depth + 1
                    where = child

    if path == False:
        return [where, global_depth, None]

    else:
        ret = []
        here = where
        while here != start:
            ret.append(here)
            here = visited[here]
        else:
            ret.append(here)

        return [where, global_depth, ret]


def get_farthest_point_from_line(line, adj) -> int:
    """주어진 직선과 adj: List[set] 으로 부터, 양 끝으로 부터 가장 먼점을 찾는다.
    이때 양 끝중, 멀리 있는 점을 max 로 처리하여 return 된다.
    max(dist_from_a, dist_from_b)

    주어진 문제가 중간값을 찾으므로, 양끝점을 제외하고 stack에 넣은뒤, (물론 양끝점은 탐색점에서 제외됨)
    해당하는 거리로 찾는다.
    """
    visited = defaultdict(int)
    stack = deque()
    global_depth = 0

    last = len(line) - 1
    for i, here in enumerate(line):
        visited[here] = here

        if i != 0 and i!= last:
            dist = max(i, last - i)
            stack.append([here, dist])

            if global_depth < dist:
                global_depth = dist
                where = here

    while len(stack):
        here, local_depth = stack.pop()

        for child in adj[here]:
            if visited[child] == 0:
                visited[child] = here
                stack.append([child, local_depth + 1])

                if global_depth < local_depth + 1:
                    global_depth = local_depth + 1
                    where = child
    
    if global_depth > last:
        return last
    else:
        return global_depth



def solution(n, edges):

    adj = [set() for _ in range(n + 1)]

    for edge in edges:
        x, y = edge
        a: set = adj[x]
        b: set = adj[y]
        a.add(y)
        b.add(x)

    first = get_farthest_point_from_point_with_path(1, adj, False)
    second = get_farthest_point_from_point_with_path(first[0], adj, True)
    k = get_farthest_point_from_line(second[2], adj)

    return k
# 
tester = tester_maker(solution)
tester()

#  아래는 문제를 풀기전 시행했던 기타 연구

class Node(object):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_Node__instance"):
            cls.__instance = dict()
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, idx) -> None:
        self.me = idx
        self.child = set()

        self.__instance[idx] = self

    @classmethod
    def instance(cls, idx):
        if not hasattr(cls, "_Node__instance"):
            cls.__instance = dict()
        
        return cls.__instance[idx]

    @classmethod
    def set_instance(cls, *args, **kwargs):
        pass


    def __str__(self):
        return f"Node [{self.me}]: {{{self.child}}}"

def dfs(adj: list, visited: DefaultDict, find: int, here: int):
    """dfs로 find를 찾으면 그 거리를 return 하는 함수
    """
    visited[here] = 1
    if find == here:
        return 0

    ret = None
    for child in adj[here]:
        if visited[child] == 0:
            ret = dfs(adj, visited, find, child)
            if isinstance(ret, int):
                return ret + 1

    return ret

def add_one(container):
    """주어진 nested list 에 대해서 +1를 하는 함수
    """
    for i, j in enumerate(container):
        if isinstance(j, list):
            add_one(j)
        else:
            container[i] += 1

def list_def(adj: list, visited: DefaultDict, here: int):
    """주어진 트리에 대해서 Nested Number Tree 로 리턴하는 함수
    """
    visited[here] = 1
    
    cond1 = len(adj[here])
    cond2 = visited[list(adj[here])[0]]
    if cond1 == 1 and cond2 == 1:
        return 0

    ret = []
    for i, child in enumerate(adj[here]):
        if visited[child] == 0:
            ret.insert(i, (list_def(adj, visited, child)))

    add_one(ret)
    return list(ret)