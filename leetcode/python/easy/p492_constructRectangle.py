class Solution:
    def constructRectangle(self, area: int):
        import math
        w = math.floor(math.sqrt(area))
        while area % w != 0 and w > 0:
            w -= 1

        return [int(area / w), w]


slu = Solution()
print(slu.constructRectangle(2))
