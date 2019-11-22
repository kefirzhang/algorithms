# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    if version >= 1:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        import math
        if n <= 1:
            return n
        helper_end = n
        helper_start = 0
        helper_middle = math.ceil((helper_end + helper_start) / 2)
        while (isBadVersion(helper_middle) is True and isBadVersion(helper_middle - 1) is False) is False:
            if isBadVersion(helper_middle) is True:
                helper_end = helper_middle
            else:
                helper_start = helper_middle

            helper_middle = math.ceil((helper_end + helper_start) / 2)
        return helper_middle
        """
        1 2 3 4 5 6 7 .... 100
        :type n: int
        :rtype: int
        """


slu = Solution()
print(slu.firstBadVersion(100))
