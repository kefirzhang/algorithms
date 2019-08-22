# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。

# 算法复杂度 不符合  这个稍后再优化 有点饿了 情绪不高 TODO TODO TODO
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merge = nums1 + nums2
        merge.sort()
        lenth = len(merge)
        if (lenth % 2 == 0):
            mid = int(lenth / 2) - 1
            return (merge[mid] + merge[mid + 1]) / 2
        else:
            mid = int((lenth + 1) / 2) - 1
            return float(merge[mid])


solution = Solution()

print(solution.findMedianSortedArrays([], [2,3]))
