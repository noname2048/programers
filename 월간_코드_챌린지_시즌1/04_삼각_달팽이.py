n = 6

class Triangle:
    number = 0
    
    idx = 0
    lv = 0

    def down(self):
        self.number += 1

        self.idx += self.lv
        self.lv += 1

    def right(self):
        self.number += 1
        self.idx += 1

    def up(self):
        self.number += 1
        self.idx -= self.lv
        self.lv -= 1

    def __getitem__(self, item):
        
        if item % 3 == 0:
            return self.down
        elif item % 3 == 1:
            return self.right
        elif item % 3 == 2:
            return self.up

def solution(n):
    answer = [0] * sum(list(range(1, n + 1)))
    triangle = Triangle()

    for rule, i in enumerate(range(n, 0, -1)):
        for _ in range(i):
            triangle[rule]()
            answer[triangle.idx] = triangle.number
            print(rule, answer)

    
    return answer

print(solution(n))