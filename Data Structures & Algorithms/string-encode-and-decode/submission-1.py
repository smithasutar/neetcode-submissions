class Solution:

    def encode(self, strs: List[str]) -> str:
        word =""

        for i in strs:
            word += i + "|"

        return word


    def decode(self, s: str) -> List[str]:
        temp =""
        List = []
        j = 0

        for i in range(0, len(s)):
            if s[i] == '|':
                List.append(temp)
                j = j+1
                temp =""
            else:
                temp += s[i]
            
        return List
