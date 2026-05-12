class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        array = []
        for idx, val in enumerate(nums):
            if val not in hashmap:
                hashmap[val] = idx
        
        # print(hashmap)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                
                sums = nums[i]+nums[j]
                diff = 0-sums
                # print(nums[i],nums[j], diff)
                if diff in nums and i!=j and j!=hashmap[diff] and i != hashmap[diff]:
                    check = sorted([nums[i],nums[j],diff])
                    print(check, array)
                    if check not in array:
                        array.append(check)
        return array
        