class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) == 1:
            return True
        leng = len(s)
        word_list = list(s)

        if self.pal_check(s) == True:
            return True

        for i in range(0, leng):
            temp = word_list[:i]+ word_list[i+1:]
            word_reg = "".join(temp)
            if self.pal_check(word_reg) == True:
                return True

        return False

    def pal_check(self, word: str) -> bool:
        leng = len(word)
        end = leng-1
        word_list = list(word)
        mid = leng//2
        for i in range(0, mid):
            temp = word_list[i]
            word_list[i] = word_list[end]
            word_list[end] = temp
            end -= 1
        
        word_reg = "".join(word_list)
        if word_reg == word:
            return True
        return False
        