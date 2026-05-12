class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len == 0:
            return False
        max_now = nums[0]
        for i in range(0, nums_len):
            if max_now <= nums[i]:
                max_now = nums[i]

        min_now = nums[0]
        for i in range(0, nums_len):
            if min_now >= nums[i]:
                min_now = nums[i]
                
        hash_map_p = [0] * (max_now+1)
        hash_map_n = [0] * ((min_now*-1)+1)

        for i in range(0, nums_len):
            if nums[i] < 0:
                pos = nums[i]*-1
                if hash_map_n[pos] != 1:
                    hash_map_n[pos] = 1
                else:
                    return True
            if nums[i] >= 0:
                if hash_map_p[nums[i]] != 1:
                    hash_map_p[nums[i]] = 1
                else:
                    return True

        return False
