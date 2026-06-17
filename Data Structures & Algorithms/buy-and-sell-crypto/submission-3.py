class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num = 100
        for p in prices:
            if p < min_num:
                min_num = p
            else:
                max_profit = max(max_profit,p-min_num)
            
        return max_profit