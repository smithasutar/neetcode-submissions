class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            total = 0
            for b in piles:
                total += math.ceil(float(b)/k)
            if total <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res        