class Solution:
    def __init__(self):
        self.helper = {}

    def minCostClimbingStairs(self, cost) -> int:
        length = len(cost)
        if length <= 2:
            return 0
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs3(self, cost) -> int:
        if len(cost) <= 2:
            return 0
        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])

    def minCostClimbingStairs2(self, cost) -> int:
        length = len(cost)
        if length <= 1:
            return 0
        if self.helper.__contains__(length):
            return self.helper[length]
        min_cost = min(
            cost[0] + self.minCostClimbingStairs(cost[1:]),
            cost[1] + self.minCostClimbingStairs(cost[2:])
        )
        self.helper[length] = min_cost
        return min_cost


slu = Solution()
print(slu.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
