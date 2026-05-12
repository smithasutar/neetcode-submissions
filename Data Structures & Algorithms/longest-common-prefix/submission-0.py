class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare prefix with each string
        for s in strs[1:]:
            # Shrink prefix until it matches the beginning of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last char
                if not prefix:
                    return ""
        
        return prefix