class Solution:
    def intersection1(self, nums1, nums2):
        helper = []
        for i in nums1:
            if i in nums2 and i not in helper:
                helper.append(i)
        return helper

    def intersection(self, nums1, nums2):
        return list(set(nums2) & set(nums1))


slu = Solution()
print(slu.intersection([1, 2, 2, 1], [2, 2]))
