class Solution:
    def __init__(self):
        self.helper = {}

    def minCostClimbingStairs(self, cost) -> int:
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
print(slu.minCostClimbingStairs([10, 15, 20]))
