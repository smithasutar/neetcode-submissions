class Solution:

    def encode(self, strs: List[str]) -> str:
        word =""
        for s in strs:
            word+=s+'.'
        return word

    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""
        for c in s:
            if c == '.':
                res.append(temp)
                temp =""
            else:
                temp += c

        return res
