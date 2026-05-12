from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = defaultdict(list)

        for i in range(0, len(nums)):
            hashmap[nums[i]].append(i)

        print(hashmap)
        for i in range(0, len(nums)):

            new = target - nums[i]

            if new in hashmap:
                print(new, nums[i])
                if i != hashmap[new][-1]:
                    result.append(i)
                    result.append(hashmap[new].pop())
                    return result

        