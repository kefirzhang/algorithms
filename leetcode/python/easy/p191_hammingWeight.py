class Solution(object):
    def hammingWeight(self, n):
        return str(bin(n)).count("1")
        """
        :type n: int
        :rtype: int
        """