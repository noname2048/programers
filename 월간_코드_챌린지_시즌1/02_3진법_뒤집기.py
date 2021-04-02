n = 19

def solution(n: int) -> int:

    tmp = ""
    while n >= 3:
        n, r = divmod(n, 3)
        tmp += str(r)
    else:
        tmp += str(n)

    return int(tmp ,3)

m = solution(n)
print(m)

"""
n = 19

def solution(n: int) -> int:

    number_list = list()
    while n >= 3:
        r = remainder = int(n % 3)
        q = quotient = int(n // 3)
        n = q

        number_list.append(r)
    else:
        number_list.append(n)

    print(number_list)
    number_list.reverse()
    print(number_list)

    s = len(number_list)

    sum = 0
    for i in range(s):
        sum += number_list[i] * pow(3, i)

    answer = sum
    return answer

m = solution(n)
print(m)
"""