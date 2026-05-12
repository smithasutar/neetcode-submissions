class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_map = list(s)
        t_map = list(t)

        s_map.sort()
        t_map.sort()

        if s_map == t_map:
            return True
        return False



        