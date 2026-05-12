class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ')': '(',
                    ']': '[',
                    '}': '{'}
        for char in s:
            if char in mapping.values(): #if an opening bracket add to stack
                stack.append(char)
            elif char in mapping: #if a closing bracket match to stack
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False
            
        if not stack:
            return True
        return False
