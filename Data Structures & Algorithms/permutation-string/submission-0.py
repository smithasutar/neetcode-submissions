class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_p = collections.Counter(s1)
        n = len(s1)
        l = 0
        r = n-1

        while r < len(s2):
            count_s = Counter(s2[l:r+1])
            if count_s == count_p:
                return True
            l+=1
            r = (l+n-1)
        return False