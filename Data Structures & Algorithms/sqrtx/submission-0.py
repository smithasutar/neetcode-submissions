class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        mini = 1
        maxi = x//2
        while mini <= maxi:
            mid = (mini+maxi)//2
            sqr = mid*mid

            if sqr == x:
                return mid
            if sqr < x:
                mini=mid+1
            if sqr > x:
                maxi=mid-1

        return maxi