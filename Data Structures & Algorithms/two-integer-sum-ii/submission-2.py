class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(numbers, start=1):
            hashmap[value] = index

        print(hashmap)

        for val in numbers:
            diff = target - val
            if diff in hashmap and hashmap[diff] != hashmap[val]:
                return[hashmap[val], hashmap[diff]]



