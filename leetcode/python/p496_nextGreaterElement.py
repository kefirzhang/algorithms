class Solution:
    def nextGreaterElement(self, nums1, nums2):
        helper = []
        for i in nums1:
            mark = False
            bigger = -1
            for j in nums2:
                if mark is True and j > i:
                    bigger = j
                    break
                elif i == j:
                    mark = True
            helper.append(bigger)
        return helper


slu = Solution()
print(slu.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
