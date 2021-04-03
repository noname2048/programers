def test(fn):
    
    test_case = [
        # [0], #  1
        # [5, 2, 3, 3, 5, 3], #  2
        # [0, 3, 3, 0, 7, 2, 0, 2, 2, 0], #  3
        # [4, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3], #  4
        # [1, 1, 1, 1], #  5
        # [2, 2, 2, 0, 0, 0, 2, 2], #  6
        # [0, 1], #  7
        # [0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4], #  8
        [0, 3, 1, 6, 0, 2, 0, 7, 1, 3, 4, 0, 5, 1, 1], #  9
    ]

    def wrapper():

        for i, a in enumerate(test_case):
            print(f"   #{i + 1:03d}")
            print(f"Q: {a}")
            ans = fn(a)
            print(f"A: {ans}")

    return wrapper

@test
def solution_fn(a):
    """문제해결전략
    01. 3개이상의 중복을 2개로 줄인다. 
    01-02. (단, 두개인 경우라도 앞쪽이나 뒤쪽에 있으면 하나로 줄인다.)
    02. 가장 많은 원소를 찾는다
    03. 해당원소 기준으로 왼쪽 먼저, 오른쪽을 탐색하여 그리디하게 찾는다.
    """

    length = len(a)
    if length < 2:
        return 0

    #  01. 3개 이상의 중복이 제거된 행렬
    new_a = list()

    i = 0
    while i < length:
        new_a.append(a[i])

        if i < length - 1 and a[i] == a[i + 1]:
            i += 1
            new_a.append(a[i])

            for j in range(i + 1, length):
                if a[i] != a[j]:
                    i = j
                    break
            else:
                i = length
        else:
            i += 1

    a = new_a
    length = len(a)

    # 01-02.
    if length > 2 and a[-1] == a[-2]:
        a = a[:-1]
        length = len(a)

    if length > 2 and a[0] == a[1]:
        a = a[1:]
        length = len(a)

    #  02. 가장 빈도가 높은 원소 찾기
    max_element_cnt = float("-inf")
    max_element = a[0]

    histo = dict()
    for _a in a:
        if _a in histo:
            histo[_a] += 1
        else:
            histo[_a] = 1

        if histo[_a] >= max_element_cnt:
            max_element_cnt = histo[_a]
            max_element = _a

    print(f"E: {max_element}")

    #  03. 원소를 기준으로 그리디하게 찾기
    pair_cnt = 0
    visited = [0] * length
    i = 0
    while i < length:
        if a[i] == max_element and visited[i] == 0:
            # 왼쪽 탐색가능
            if i > 0 and visited[i - 1] == 0 and a[i - 1] != max_element:
                visited[i - 1], visited[i] = 1, 1
                i += 1
                pair_cnt += 1
            # 오른쪽 탐색 가능
            elif i < length - 1 and a[i + 1] != max_element:
                visited[i], visited[i + 1] = 1, 1
                i += 2
                pair_cnt += 1
            else:
                i += 1
        else:
            i += 1
    
    return pair_cnt * 2

solution_fn()

"""
마지막 점검 (2021.04.03)을 하면서 테스트 28번만 틀리는 것을 확인했습니다.
해당 문제는 부호 하나를 바꿔서 맞췄는데요 (> 를 >= 로)
이상함을 느껴 곰곰이 생각해 보았습니다.

28번 까지의 모든 테스트 케이스를 통과했지만,
제가 생각한 테스트 케이스 반례는 오답이 나왔습니다.

가상의 28: `[0, 0, 3, 1, 2, 1, 3, 4, 0, 1, 4]` 답 : 6, 첨부코드: 6
가상의 29: `[0, 3, 1, 6, 0, 2, 0, 7, 1, 3, 4, 0, 5, 1, 1]` __답: 8, 첨부코드: 6__
__28까지의 테스트케이스 (모두)통과: (정답처리)__

해당 케이스는 가장 많은 원소를 기준으로 탐색을 진행할 때,
빈도수가 같은 원소가 존재할 경우, (예1: 0이 3개, 1이 3개)
둘 중에 하나를 골라 고려하는 경우 오답이 될 수 있습니다.


해당 원소가 리스트의 맨앞 혹은 맨뒤에 두 번 이상 연속 나타날 때
발생하는 문제로, 
그리디 방식으로 문제를 해결하는 사람은 
1. 빈도수가 같은 원소에 대해서도 고려하거나, 
2. 맨앞, 혹은 맨뒤 두개 이상의 중복에 대해 처리하여야

정답으로 인정될 수 있도록 테스트 케이스를 추가 해야합니다.
"""