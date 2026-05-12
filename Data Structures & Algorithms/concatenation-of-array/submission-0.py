class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans_len = n*2
        ans = [0] * ans_len
        for i in range(0, ans_len):
            j = i
            if i >= n:
                j = j - n
            ans[i] = nums[j]
            
        return ans    