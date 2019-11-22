class Solution:
    def findMaxAverage(self, nums, k) -> float:
        max_average = 0
        i, pre_total = k, sum(nums[:k])
        max_average = pre_total / k
        # print(max_average)
        while i < len(nums):
            pre_total = pre_total + nums[i] - nums[i - k]
            max_average = max(max_average, pre_total / k)
            # print(i, max_average)
            i += 1

        return max_average


slu = Solution()
print(slu.findMaxAverage([4, 2, 1, 3, 3], 2))
