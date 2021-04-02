a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
a = [9,-1,-5]

def solution(a):
    answer, left_answer, right_answer = 0, 0, 0

    center_idx = 0
    center_m = a[center_idx]

    for i, _a in enumerate(a):
        if _a < center_m:
            center_idx = i
            center_m = _a

    left_local_min = a[0]

    for i in range(center_idx):
        if a[i] <= left_local_min:
            
            left_local_min = a[i]
            left_answer += 1

    right_local_min = a[-1]
    for i in range(len(a) - 1, center_idx, -1):
        if a[i] <= right_local_min:

            right_local_min = a[i]
            right_answer += 1

    answer = left_answer + right_answer + 1
    return answer

print(solution(a))
