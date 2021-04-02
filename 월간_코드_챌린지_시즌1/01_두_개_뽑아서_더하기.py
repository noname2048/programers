numbers = [2,1,3,4,1]
print(numbers)

s = len(numbers)

new_set = set()

for i in range(s):
    for j in range(i + 1, s):
        new_set.add(numbers[i] + numbers[j])
        
new_list = list(new_set)
print(new_list)
