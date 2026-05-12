from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for value in nums:
            if value in hashmap:
                hashmap[value] += 1
                #print(hashmap)
                return True
            else:
                hashmap[value] = 0

        #print(hashmap)
        return False 