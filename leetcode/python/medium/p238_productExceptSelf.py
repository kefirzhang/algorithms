class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0] * n
        k = 1
        for i in range(n):
            res[i] = k
            k = k * nums[i]
        k = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * k
            k = k * nums[i]
        return res


slu = Solution()
print(slu.productExceptSelf([1, 2, 3, 4]))
