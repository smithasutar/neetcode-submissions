class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temper = []
        temp = ""
        for c in s:
            if c in temp:
                temper.append(temp)
                temp = temp[temp.index(c)+1:]
            temp += c
        temper.append(temp)  # Make sure to include the last substring
        large = max(temper, key=len)
        return len(large)