s = "110010101001"

def solution(s):
    answer = [0, 0]
    cnt, zero = 0, 1

    while s != "1":
        answer[cnt] += 1

        one_s = 0
        for _s in s:
            if _s == "0":
                answer[zero] += 1
            else:
                one_s += 1
        
        s = str(bin(one_s))[2:]

    return answer

print(solution(s))