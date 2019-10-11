import math
# TODO

class Solution:
    def findNearBy(self, n, heaters):
        if n <= heaters[0]:
            return heaters[0]
        elif n >= heaters[-1]:
            return heaters[-1]

        length = len(heaters)
        start = 0
        end = length - 1
        middle = math.ceil((start + end) / 2)
        while heaters[middle] == n or (
                heaters[middle - 1] - n < abs(heaters[middle] - n) and abs(heaters[middle] - n) > abs(
            heaters[middle + 1] - n)):
            if 1:
                1

    def findRadius(self, houses, heaters) -> int:
        heaters.sort()
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
