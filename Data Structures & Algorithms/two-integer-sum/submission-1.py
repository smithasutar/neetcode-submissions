from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            result = target-num
            if result in hashmap:
                return [hashmap[result], i]
            else:
                hashmap[num] = i

















        