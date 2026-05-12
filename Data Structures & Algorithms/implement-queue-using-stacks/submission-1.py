class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2 = list(reversed(self.stack1))

    def pop(self) -> int:
        self.stack2.pop()
        return self.stack1.pop(0)

    def peek(self) -> int:

        return self.stack1[0]

    def empty(self) -> bool:
        return not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()