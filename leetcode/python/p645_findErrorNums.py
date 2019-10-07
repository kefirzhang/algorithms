class Solution:
    def findErrorNums(self, nums):

        helper = [0] * len(nums)

        for i in nums:
            helper[i - 1] += 1

        for i, n in enumerate(helper):
            print(i, n)
            if n == 0:
                lack = i + 1
            elif n == 2:
                more = i + 1

        return [more, lack]


slu = Solution()
print(slu.findErrorNums([1, 2, 2, 4]))
