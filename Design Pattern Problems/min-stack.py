# 📌 Requirements
#
# Implement a stack that supports:
#
#     1.push(x)
#     2.pop()
#     3.top()
#     4.getMin()

class MinStack:

    def __init__(self):
        self.stk = []

    def peek(self):
        return self.stk[-1][0]

    def pop(self):
        return self.stk.pop()[0]

    def push(self, x: int):
        if not self.stk:
            self.stk.append((x, x))
            return

        currMin = min(x, self.stk[-1][1])
        self.stk.append((x, currMin))

    def getMin(self):
        return self.stk[-1][1] if self.stk else None

