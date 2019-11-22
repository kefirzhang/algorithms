# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    if num == 6:
        return 0
    elif num > 6:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n):
        import math
        if n <= 1:
            return n
        helper_end = n
        helper_start = 0
        helper_middle = math.ceil((helper_end + helper_start) / 2)
        while guess(helper_middle) != 0:
            if guess(helper_middle) == 1:
                helper_start = helper_middle
            else:
                helper_end = helper_middle
            helper_middle = math.ceil((helper_end + helper_start) / 2)
        return int(helper_middle)
        """
        1 2 3 4 5 6 7 .... 100
        :type n: int
        :rtype: int
        """


slu = Solution()
print(slu.guessNumber(10))
