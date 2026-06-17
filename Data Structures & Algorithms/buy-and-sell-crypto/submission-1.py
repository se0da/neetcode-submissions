class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            
            maxP = max(maxP, price-lowest)
        
        return maxP
        