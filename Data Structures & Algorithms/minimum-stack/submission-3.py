class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        print("add", self.stack)
        

    def pop(self) -> None:
        print("pop", self.stack[len(self.stack)-1])
        self.stack.pop()
        

    def top(self) -> int:
        print("top", self.stack[len(self.stack)-1])
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        val = min(self.stack)
        print("min", self.stack, val)
        
        return val
        
