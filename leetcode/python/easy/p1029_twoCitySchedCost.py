class Solution:
    def twoCitySchedCost(self, costs) -> int:
        for i in range(len(costs) - 1):
            j = i + 1
            while j < len(costs):
                x = abs(costs[i][0] - costs[i][1])
                y = abs(costs[j][0] - costs[j][1])
                if x > y:
                    costs[i], costs[j] = costs[j], costs[i]
                j += 1
        city1 = 0
        city2 = 0
        ans = 0
        i = len(costs) - 1
        while i >= 0:
            if costs[i][0] < costs[i][1] and city1 < len(costs)/2:
                city1 += 1
                ans += costs[i][0]
            elif city2 < len(costs)/2:
                city2 += 1
                ans += costs[i][1]
            else:
                city1 += 1
                ans += costs[i][0]
            i -= 1
        return ans


slu = Solution()
print(slu.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
