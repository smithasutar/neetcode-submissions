class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int: 
        length = 0 
        l = 0 
        count = [-1]* 128 
        largest_len = 0 
        for r in range(len(s)):

            if count[ord(s[r])] >= l:
                
                largest_len = max(length, largest_len) 
                l = count[ord(s[r])]+1
                length = r-l 
                
            
            length += 1 
            count[ord(s[r])] = r 
            
        
        largest_len = max(length, largest_len) 
            
        return largest_len