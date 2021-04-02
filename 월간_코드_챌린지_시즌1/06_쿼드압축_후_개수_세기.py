import math
import itertools

a = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
a = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
a = [[0,0], [0,0]]

def recur(a):
    ed = len(a)
    st, mi = 0, int(ed // 2)

    print(f"level {ed}")

    if ed == 2:
        if type(a[0][0]) == int:
            if a[0][0] == a[0][1] == a[1][0] == a[1][1]:
                return a[0][0]
        
        return a                 
    else:      
        ret = [
            recur([a[r][st:mi] for r in range(st, mi)]),
            recur([a[r][mi:ed] for r in range(st, mi)]),
            recur([a[r][st:mi] for r in range(mi, ed)]),
            recur([a[r][mi:ed] for r in range(mi, ed)]),
        ]

        if isinstance(ret[0], int) and ret[0] == ret[1] == ret[2] == ret[3]:
            return ret[0]

        return ret

def flatten(container):
    if isinstance(container, (list, tuple)):
        for i in container:
            if isinstance(i, (list, tuple)):
                for j in flatten(i):
                    yield j
            else:
                yield i
    else:
        yield container

def solution(a):
    quad = recur(a)
    flat = list(flatten(quad))

    answer = [0, 0]
    for i in flat:
        if i == 0:
            answer[0] += 1
        elif i == 1:
            answer[1] += 1

    return answer
    
print(solution(a))


