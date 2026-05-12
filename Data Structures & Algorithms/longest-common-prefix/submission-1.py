class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):

                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        
        return prefix
