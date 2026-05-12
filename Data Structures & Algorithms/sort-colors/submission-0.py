class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        l, r = 0, len(nums)-1

        while i <= r:
            if nums[i] == 0:
                #swap l and i
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l +=1

            elif nums[i] == 2:
                #swap r and i
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                r -= 1
                i-=1
            
            i+=1
        