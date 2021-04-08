s = "baby"
s = "skkks"
s = "skkkk"
s = "skkks"
s = "apple"
s = "akyeenaeona"

ls = len(s)

def solution(s):
    answer = 0
    return 0

for i in range(ls):
    for j in range(i + 1, ls + 1):
        print(s[i:j])

right_first_diff = [None for _ in range(ls)]
left_first_diff = [None for _ in range(ls)]

#  RFDI right_first_differnt_index
j = 0
for i in range(ls):
    if s[j] != s[i]:
        while j != i:
            right_first_diff[j] = i
            j += 1

while j < ls:
    right_first_diff[j] = -1
    j += 1

#  LFDI left_first_different_index
j = ls - 1
for i in range(ls - 1, -1, -1):
    if s[j] != s[i]:
        while j != i:
            left_first_diff[j] = i
            j -= 1
while j > -1:
    left_first_diff[j] = -1
    j -= 1

print(right_first_diff)
print(left_first_diff)