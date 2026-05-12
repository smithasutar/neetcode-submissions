class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = int(a, 2)
        num2 = int(b, 2)

        return bin(num+num2)[2:]
        