
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

adj = [set() for _ in range(n + 1)]

for edge in edges:
    x, y = edge
    a: set = adj[x]
    b: set = adj[y]
    a.add(y)
    b.add(x)


def dist(a, b):
    global n
    visited = [0 for _ in range(n + 1)]
    visited[a] = 1

    for child_a in adj[a]:
        if visited[child_a] == 0:
            pass

def dfs(adj: list, visited: DefaultDict, find: int, here: int):

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
    for i, j in enumerate(container):
        if isinstance(j, list):
            add_one(j)
        else:
            container[i] += 1

def list_def(adj: list, visited: DefaultDict, here: int):
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
