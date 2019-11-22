class Solution:
    def maxProfit(self, prices):
        total = 0
        if len(prices) == 0:
            return total

        length = len(prices)
        i = 0
        while i < length - 1:
            if prices[i] < prices[i + 1]:
                total += prices[i + 1] - prices[i]
            i += 1

        return total


slu = Solution()
print(slu.maxProfit([7, 1, 5, 3, 6, 4]))
