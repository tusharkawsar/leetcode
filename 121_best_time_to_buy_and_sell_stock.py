class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 0: return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for item in prices:
            min_price = min(min_price, item)
            max_profit = max(max_profit, item-min_price)
            
            print(max_profit, min_price)
            
        return max_profit
        
