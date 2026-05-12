class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = list(s)
        ss= list(s)
        n = len(s)
        right = n-1
        mid = n//2
        for i in range(right+1):
            word[i] = ss[right]
            right-=1
        comp = "".join(word)
        s = s.lower()
        comp = comp.lower()
        old = ""
        new =""
        for ch in s:
            if ch.isalnum():
                old += ch
        for ch in comp:
            if ch.isalnum():
                new += ch
            
        if old == new:
            return True
        else:
            return False