class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        highest_profit = 0
        l = 0

        for r in range(0, len(prices)):
            
            if prices[r] < smallest:
                l = r
                smallest = prices[l]
                
            highest_profit = max((prices[r]-smallest), highest_profit)

        return highest_profit
            

        