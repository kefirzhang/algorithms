class Solution:

    def subsets(self, nums):
        res = [[]]
        for i in nums:
            for j in res:
                res = res + [j + [i]]
        return res


slu = Solution()
print(slu.subsets([1, 2, 3]))
