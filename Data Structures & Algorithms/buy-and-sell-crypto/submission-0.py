class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = set()

        for L in range(len(prices)):
            maxi = 0
            
            for R in range(L, len(prices)):
                
                if prices[R] - prices[L] > maxi:
                    maxi = prices[R] - prices[L]
            
            profit.add(maxi)
            
        return max(profit)

        