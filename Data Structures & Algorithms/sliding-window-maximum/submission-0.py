class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_win = []

        for l in range(len(nums)-k+1):
            r = l+k
            val = max(nums[l:r])
            max_win.append(val)

        return max_win