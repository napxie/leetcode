class SortedStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        while self.stack1 and self.stack1[-1] < val:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(val)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> None:
        if not self.stack1:
            return
        self.stack1.pop()

    def peek(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1[-1]

    def isEmpty(self) -> bool:
        return len(self.stack1) == 0


class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.swim(len(self.stack)-1)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack[0], self.stack[-1] = self.stack[-1], self.stack[0]
        self.stack.pop()
        self.sink(0)

    def peek(self) -> int:
        return self.stack and self.stack[0] or -1

    def isEmpty(self) -> bool:
        return not self.stack

    def sink(self, index):
        n = len(self.stack)
        while 2*index+1 < n:
            j = 2*index+1
            if j < n-1 and self.stack[j] > self.stack[j+1]:
                j += 1
            if self.stack[index] <= self.stack[j]:
                break
            self.stack[index], self.stack[j] = self.stack[j], self.stack[index]
            index = j

    def swim(self, index):
        while index > 0 and self.stack[index] < self.stack[(index-1)//2]:
            self.stack[index], self.stack[(
                index-1)//2] = self.stack[(index-1)//2], self.stack[index]
            index = (index-1)//2


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
