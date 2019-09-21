class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        a, b, c = nums[:3]  # 前三个
        e, d, f = nums[-3:]  # 后三个
        return max(e * d * f, a * b * f)


slu = Solution()
print(slu.maximumProduct([1, 2, 2, 3]))
