class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        digit = n
        val = 0
        sums = 0

        while n > 0:
            digit = n % 10
            val = digit*digit
            sums+=val
            print(sums)
            n //= 10
            if n <= 0:
                if sums == 1:
                    return True
                if sums in seen:
                    print("here", val, seen)
                    return False
                seen.append(sums)
                n = sums
                sums = 0

        return False
        