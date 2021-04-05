
from collections import defaultdict
from typing import DefaultDict


n = 4
edges = [[1, 2], [2, 3], [3, 4]]

n = 5
edges = [[1,5],[2,5],[3,5],[4,5]]
"""
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


    def __str__(self):
        return f"Node [{self.me}]: {{{self.child}}}"
    

def solution(n, edges):

    root = Node(1)

    for edge in edges:
        p, c = edge[0], edge[1]
        node = Node.instance(p)
        if node:
           node.child.add(c)
        else:
            node = Node(p)
            node.child.add(c)
        
    return root

solution(n, edges)
"""
#  01 트리 지름 구하기, 이때 dfs, bfs 는 중요하지 않음, 경로 저장
#  02 트리 지름으로 부터 제일 멀리 떨어진 거리 구하기 (이때의 두개의 점을 저장), 없으면 04로
#  03 해당점으로 부터 거리 a, b, c 를 구함 이때 b가 지름 밖에 있으면 a-c나 a-b가 답이 됨 
#  04 지름 - 1 는 정답
adj = [set() for _ in range(n + 1)]

for edge in edges:
    x, y = edge
    a: set = adj[x]
    b: set = adj[y]
    a.add(y)
    b.add(x)


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

visited = defaultdict(int)
print(dfs(adj, visited, 4, 1))

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

visited = defaultdict(int)
print(list_def(adj, visited, 1))

from collections import deque
def get_farthest_point_from_point_with_path(start, adj, path=False):
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

ans_a = get_farthest_point_from_point_with_path(1, adj, False)
print(ans_a)
ans_b = get_farthest_point_from_point_with_path(ans_a[0], adj, True)
print(ans_b)

from typing import List
def get_farthest_point_from_line(line: list[int], adj: List[set]) -> int:
    visited = defaultdict(int)
    stack = deque()

    for l in line:
        visited[l] = l
        stack.append([l, 0])
       
    global_depth = 0
    where = line[1]

    while len(stack):
        here, local_depth = stack.pop()

        for child in adj[here]:
            if visited[child] == 0:
                visited[child] = here
                stack.append([child, local_depth + 1])
                
                if global_depth < local_depth + 1:
                    global_depth = local_depth + 1
                    where = child

    #  find parent
    here = where
    while visited[here] != here:
        here = visited[here]
    parent = here

    start_from = line.index(parent)
    return [where, global_depth, parent, start_from]

print(get_farthest_point_from_line(ans_b[2], adj))

def solution(n, edges):

    adj = [set() for _ in range(n + 1)]

    for edge in edges:
        x, y = edge
        a: set = adj[x]
        b: set = adj[y]
        a.add(y)
        b.add(x)
    
    radius_start, _, _ = get_farthest_point_from_point_with_path(1, adj, False)
    radius_end, radius, line = get_farthest_point_from_point_with_path(radius_start, adj, True)
    c, sub_radius, x, ax = get_farthest_point_from_line(line, adj)

    a = radius_start
    b = radius_end
    bx = radius - ax
    cx = sub_radius

    ab = radius
    ac = ax + cx
    bc = bx + cx

    ret = [ab, ac, bc]
    ret.sort()

    return ret[1]

print(solution(n, edges))
