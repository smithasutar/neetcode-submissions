class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        col = []
        while n > 0:
            n-=1
            val = n%26
            col.append(chr(ord('A') + val))
            n //= 26
        col.reverse()
        word = "".join(col)
        return word
