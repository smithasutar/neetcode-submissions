class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        temper = []

        for c in s:
            if c in temp:
                temper.append(temp)
                temp = temp[temp.index(c)+1:]
            temp += c
        temper.append(temp)
        maxi = max(temper, key=len)
        return len(maxi)
