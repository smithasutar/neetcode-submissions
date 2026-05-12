class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
            
        need_dic = defaultdict(int)
        have_dic = defaultdict(int)
        
        have = 0
        min_len = float("inf")
        min_word = ""
       
        for i in range(len(t)):
            need_dic[t[i]] += 1

        need = len(need_dic)
        l = 0

        for r in range(len(s)):

            if s[r] in need_dic:
                have_dic[s[r]] += 1
                if have_dic[s[r]] == need_dic[s[r]]:
                    have+=1

            while have == need:
                if r-l+1 < min_len:
                    min_len = r-l+1
                    min_word = s[l:r+1]
                if s[l] in need_dic:
                    have_dic[s[l]] -= 1
                    if have_dic[s[l]] < need_dic[s[l]]:
                        have-=1
                l+=1

        return min_word