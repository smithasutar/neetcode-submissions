class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            bit = bin(i)[2:]
            one = bit.count('1')
            res.append(one)

        return res
        