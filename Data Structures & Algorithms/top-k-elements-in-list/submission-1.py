class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        lists = [0]*k

        n= len(nums)
        for i in range(n):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1

        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            lists[i] = sorted_items[i][0]

        return lists

            


        