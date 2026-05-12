class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = [0] * 127
        hash_t = [0] * 127

        s_len = len(s)
        t_len = len(t)

        for i in range(0, s_len):
            hash_s[ord(s[i])] += 1

        for i in range(0, t_len):
            hash_t[ord(t[i])] += 1

        for i in range(0, 127):
            if hash_s[i] != hash_t[i]:
                return False
        
        return True