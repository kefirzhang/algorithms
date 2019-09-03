class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        if len(prices) == 0:
            return max_profit
        min_point = prices[0]
        for i in prices:
            if i < min_point:
                min_point = i
            if i > min_point:
                max_profit = max(max_profit, i - min_point)
        return max_profit


slu = Solution()
print(slu.maxProfit([]))
