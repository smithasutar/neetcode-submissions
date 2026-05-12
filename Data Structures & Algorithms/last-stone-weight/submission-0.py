class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
            
        for i in range(len(stones)):
            stones[i] = stones[i]*-1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            val1 = -heapq.heappop(stones)
            val2 = -heapq.heappop(stones)
            diff = val1 - val2
            heapq.heappush(stones, -diff)

        return -heapq.heappop(stones)        
        