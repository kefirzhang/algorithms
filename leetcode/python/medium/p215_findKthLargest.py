class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort()
        return nums[::-1][k - 1]

slu = Solution()
print(slu.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
