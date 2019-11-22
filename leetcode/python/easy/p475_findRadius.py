import math


class Solution2:
    def findNearBy(self, n, heaters):
        if n <= heaters[0]:
            return heaters[0]
        elif n >= heaters[-1]:
            return heaters[-1]

        length = len(heaters)
        start = 0
        end = length - 1
        middle = math.floor((start + end) / 2)
        while (heaters[middle] <= n <= heaters[middle + 1]) is False:
            print(middle, heaters[middle], heaters[middle + 1], n)
            if heaters[middle] > n:
                end = middle
            else:
                start = middle
            middle = math.floor((start + end) / 2)

        if n - heaters[middle] < heaters[middle + 1] - n:
            return heaters[middle]
        else:
            return heaters[middle + 1]

    def findRadius(self, houses, heaters) -> int:
        heaters.sort()
        helper = []
        for house in houses:
            distance = abs(self.findNearBy(house, heaters) - house)
            helper.append(distance)
        return max(helper)


class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        len_house = len(houses)
        len_heaters = len(heaters)
        i = 0
        j = 0
        ans = 0  # 最小距离

        while i < len_house and j < len_heaters:
            if houses[i] <= heaters[j]:
                ans = max(ans, heaters[j] - houses[i])
                i += 1
            else:
                if j == len_heaters - 1:
                    ans = max(ans, houses[i] - heaters[j])
                    i += 1
                else:
                    if heaters[j] < houses[i] <= heaters[j + 1]:
                        ans = max(ans, min(houses[i] - heaters[j], heaters[j + 1] - houses[i]))
                        i += 1
                    else:
                        j += 1

        return ans


slu = Solution()
print(slu.findRadius([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923],
                     [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840,
                      143542612]))
# print(slu.findNearBy(3, [1, 4]))
'''
[282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
'''
