class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        helper_end = num
        helper_start = 0
        helper_middle = math.ceil((helper_start + helper_end) / 2)

        while helper_middle * helper_middle != num:
            print(helper_start, helper_end, helper_middle)
            if helper_middle * helper_middle > num:
                helper_end = helper_middle
            else:
                helper_start = helper_middle
            helper_middle = math.ceil((helper_start + helper_end) / 2)
            if helper_middle == helper_start or helper_middle == helper_end:
                return False

        return True


slu = Solution()
print(slu.isPerfectSquare(1))
