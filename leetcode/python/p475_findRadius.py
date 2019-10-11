class Solution:
    def findRadius(self, houses, heaters) -> int:
        helper = []
        for house in houses:
            distance = False
            for heater in heaters:
                if distance is False:
                    distance = abs(heater - house)
                else:
                    distance = min(distance, abs(heater - house))
            helper.append(distance)
        return max(helper)


slu = Solution()
print(slu.findRadius([1, 2, 3], [2]))
