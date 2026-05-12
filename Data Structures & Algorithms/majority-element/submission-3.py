class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0

            hashmap[nums[i]] += 1
        max_count = 0
        max_num = None

        for num in hashmap:
            if hashmap[num] > max_count:
                max_count = hashmap[num]
                max_num = num

        return max_num