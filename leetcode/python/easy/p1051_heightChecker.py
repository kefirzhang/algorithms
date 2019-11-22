class Solution:
    def heightChecker(self, heights):
        pre_helper = heights[:]
        heights.sort()
        num = 0
        for i, n in enumerate(heights):
            if n != pre_helper[i]:
                num += 1

        return num


slu = Solution()
print(slu.heightChecker([1, 1, 4, 2, 1, 3]))
