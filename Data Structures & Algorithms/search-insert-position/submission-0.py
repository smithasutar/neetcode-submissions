class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mini = 0
        maxi = len(nums)-1

        while mini <= maxi:
            mid = (mini+maxi)//2
            if nums[mid] < target:
                mini = mid+1
            if nums[mid] > target:
                maxi = mid-1
            if nums[mid] == target:
                return mid

        return mini
        