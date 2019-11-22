class Solution:
    def intersect(self, nums1, nums2):
        helper = []
        for i in nums1:
            if i in nums2:
                helper.append(i)
                nums2.remove(i)
        return helper


# 当然有更优的算法  hashmap 或者 排序后  双指针 都可以 这里难度先过

slu = Solution()
print(slu.intersect([1, 2, 2, 1], [2, 2]))
