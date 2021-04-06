from collections import defaultdict, deque
from typing import DefaultDict, List
from time import time

def tester_maker(solution):

    n_list = [4, 5, 6, 7, 16, 14, 14]
    edges_list = [
        [[1, 2], [2, 3], [3, 4]],
        [[1, 5], [2, 5], [3, 5], [4, 5]],
        [[1, 6], [2, 3], [3, 5], [3, 4], [2, 6]],
        [[1, 2], [2, 3], [2, 4], [1, 5], [5, 7], [5, 6]],
        [[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[2, 11],[11, 13],
            [11, 12],[3, 14],[4, 15],[15, 16],[5, 9],[9, 10],],
        [[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[8, 9],[5, 11],[11, 12],[6, 13],[13, 14],],
        [[1, 2],[2, 3],[3, 4],[4, 5],[5, 6],[6, 7],[7, 8],[8, 9],[4, 11],[11, 12],[5, 13],[13, 14],],
    ]

    def wrapper():
        
        for i, n in enumerate(n_list):
            print(f"#{i + 1:03d}")
            st = time()
            ret = solution(n, edges_list[i])
            run_time = time() - st
            print(f"time takes {int(run_time * 1000)} ms")
            print()

    return wrapper


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

    print(f"start a. {a}")
    print(f"ends b. {b}")
    print(f"center x. {x}")
    print(f"center c. {c}")
    print(f"ab, ac, bc {ab} {ac} {bc}")

    ret = [ab, ac, bc]
    ret.sort()

    print(f"ans {ret[1]}")

    return ret[1]

tester = tester_maker(solution)
tester()




