def solution(a):
    answer = -1
    return answer


def tester_makeer(solution):

    a_list = [
        [[0,1,0],[1,1,1],[1,1,0],[0,1,1]],
    ]

    def wrapper(a):
        for i, a in enumerate(a_list):
            ans = solution(a)
            print(f"#{i:03d} ans: {ans}")

    return wrapper

"""
ncr_debug = False
dp_debug = True
dv = pow(10, 7) + 19
"""
a = [[0,1,0],[1,1,1],[1,1,0],[0,1,1]]
a = [[1,0,0],[1,0,0]]
a = [[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]
a = [[0, 1, 1]]
"""
rows = len(a)
cols = len(a[0])

ones_in_col = [0 for _ in range(cols)]
for c in range(cols):
    for r in range(rows):
        ones_in_col[c] += a[r][c]

dp_cache = [[0 for c in range(cols)] for r in range(rows + 1)]
ncr_cache = [[None for c in range(rows + 1)] for r in range(rows + 1)]
"""

from collections import deque
def ncr(cache, n, r, dv, ncr_debug=False):
    """ nCr을 구하는 함수.
    (n)C(r) = (n-1)C(r) + (n-1)C(r-1)

    재귀를 안쓰고 스택으로 풀어보았다.
    재귀와 다른점은 return 대신에 stack.pop을 쓰고
    while 문을 이어가는것
    """
    
    stack = deque()
    stack.append([n, r])

    while len(stack):
        n, r = stack[-1]

        if cache[n][r] is None:
            print(f"{n}C{r}") if ncr_debug else None

            """base 조건
            1Cx = 1
            nC0 = 1
            nCn = 1
            nC1 = n
            """
            if n == 1 or r == 0:
                cache[n][r] = 1
                stack.pop()

            elif n == r:
                cache[n][r] = 1
                stack.pop()
            
            elif r == 1:
                cache[n][r] = n
                stack.pop()

            else:
                if cache[n - 1][r] is None:
                    stack.append([n - 1, r])
                    print(f"+{n  - 1}C{r}") if ncr_debug else None

                if cache[n - 1][r - 1] is None:
                    stack.append([n - 1, r - 1])
                    print(f"+{n - 1}C{r - 1}") if ncr_debug else None

                if cache[n - 1][r] is not None and cache[n - 1][r - 1] is not None:
                    cache[n][r] = (cache[n - 1][r] % dv + cache[n - 1][r - 1] % dv) % dv
                    stack.pop()
        else:      
            stack.pop()
    
    return cache[n][r]

"""
# init
first_even = rows - ones_in_col[0]
for i in range(rows):
    dp_cache[i][0] = ncr(ncr_cache, rows, first_even) if i == first_even else 0

print("init") if dp_debug else None
#  go
#  c = [0:cols - 2]
for here in range(cols - 1):
    next = here + 1
    ones = ones_in_col[next]
    print(f"#cols: {here} next_ones: {ones}") if dp_debug else None

    for even in range(0, rows + 1):
        odds = rows - even

        print(f"dp_cache[e={even}][{here}] = {dp_cache[even][here]}") if dp_debug else None

        #  select_from_even = [0:ones]
        for select_from_even in range(ones + 1):
            select_from_odds = ones - select_from_even

            if even >= select_from_even and odds >= select_from_odds:
                new_even = (even - select_from_even) + select_from_odds

                print(f"select(e:{select_from_even}, o:{select_from_odds})=>dp_cache[{new_even}][{next}]") if dp_debug else None
                dp_cache[new_even][next] += (
                    dp_cache[even][here] * 
                    ncr(ncr_cache, even, select_from_even) *
                    ncr(ncr_cache, odds, select_from_odds)
                )

print(f"ans {dp_cache[rows][cols - 1]}")
print(f"ans {dp_cache[rows][cols - 1]}")
"""

def solution(a):

    dv = pow(10, 7) + 19
    rows, cols = len(a), len(a[0])

    ones_in_col = [0 for _ in range(cols)]
    for c in range(cols):
        for r in range(rows):
            ones_in_col[c] += a[r][c]

    #  n := 0 ~ rows, r := 0 ~ rows
    ncr_cache = [[None for c in range(rows + 1)] for r in range(rows + 1)]
    #  r := 0개 ~ rows개, c := 0 ~ (cols - 1)
    dp_cache = dp_cache = [[0 for c in range(cols)] for r in range(rows + 1)]

    #  result of first column is fixed
    first_even = rows - ones_in_col[0]
    for i in range(rows + 1):
        dp_cache[i][0] = ncr(ncr_cache, rows, first_even, dv) if i == first_even else 0

    #  Then, here := 0 ~ cols - 2 (col - 1 is last, so before last)
    for here in range(cols - 1):
        next = here + 1
        ones = ones_in_col[next]

        #  even := 0 ~ rows
        for even in range(0, rows + 1):
            odds = rows - even

            #  e, o := [0, ones] ~ [ones, 0]
            for select_from_even in range(ones + 1):
                select_from_odds = ones - select_from_even

                #  if dp_cache[even][here] is acceptable
                if even >= select_from_even and odds >= select_from_odds:
                    new_even = (even - select_from_even) + select_from_odds

                    dp_cache[new_even][next] += (
                        (dp_cache[even][here] % dv) * 
                        ncr(ncr_cache, even, select_from_even, dv) *
                        ncr(ncr_cache, odds, select_from_odds, dv)
                    )
                    
    return dp_cache[rows][cols - 1]

print(solution(a))
