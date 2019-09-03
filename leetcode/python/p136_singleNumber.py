class Solution:
    def singleNumber(self, nums):
        n = 0
        for i in nums:
            n = i^n
        return n


slu = Solution()
print(slu.singleNumber([2, 2, 2,2]))
