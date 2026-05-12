class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if word1 == "":
            return word2
        if word2 == "":
            return word2
        
        combine_len = len(word1)+len(word2)
        one = 0
        two = 0
        temp = []
        one_list = list(word1)
        two_list = list(word2)
        for i in range(combine_len):
            if i%2 == 0:
                if one >= len(word1):
                    temp += two_list[two]
                    two+=1
                    # print("REST of two", temp)
                else :
                    temp += one_list[one]
                    one+=1
                    # print("add one", temp)
                
            if i%2 != 0:
                if two >= len(word2):
                    temp += one_list[one]
                    one+=1
                    # print("REST of one", temp, i, len(word2), two)
                else:
                    temp += two_list[two]
                    two+=1
                    # print("add two", temp)
        word = "".join(temp)
        return word
        