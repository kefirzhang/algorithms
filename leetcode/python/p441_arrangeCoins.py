class Solution:
    def getLevelNum(self, level):
        return ((1 + level) * level) / 2

    def arrangeCoins(self, n: int) -> int:
        import math
        if n <= 1:
            return n
        helper_end = n
        helper_start = 0
        helper_middle = math.ceil((helper_start + helper_end) / 2)

        while (self.getLevelNum(helper_middle) <= n < self.getLevelNum(helper_middle + 1)) is False:
            print(helper_middle, helper_start, helper_end)
            if self.getLevelNum(helper_middle) > n:
                helper_end = helper_middle
            else:
                helper_start = helper_middle
            helper_middle = math.ceil((helper_start + helper_end) / 2)
        return helper_middle


slu = Solution()
print(slu.arrangeCoins(2))
