class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        top = self.data.pop()
        if self.helper and top == self.helper[-1]:
            self.helper.pop()
        return top

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


if __name__ == "__main__":
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
