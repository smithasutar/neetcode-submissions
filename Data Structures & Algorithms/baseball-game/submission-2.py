class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        i = 0
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
            i+=1
        return sum(stack)




        