class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # use sliding window approach
        i = 0
        j = 1
        max_profit = 0

        while j < len(prices):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
            
            if prices[j] >= prices[i]:
                j += 1
            else:
                i += 1
            
        
        return max_profit
