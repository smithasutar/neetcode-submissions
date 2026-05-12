from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # iterate through the array ad find the largest value
        # set highest as the length of the hashmapP and hashmapN
        # start at index 0
        # if arr0 is negative
        #     then 
        #         if target is negative
        #             then target*-1 - arr0*-1 and search in hashmapN
        #         if target is positive
        #             then target + arr0 and search in hashmapP

        # if arr0 is positive
        #     then
        #         if target is negative
        #             then target + arr0*-1 and search in hashmapN
        #         if target is positive
        #             then target - arr0 and search in hashmapP


        hashmap = {}  # number -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

















        