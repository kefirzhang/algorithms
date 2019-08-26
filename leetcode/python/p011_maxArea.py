class Solution:
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


slu = Solution()
# print(slu.maxArea([2, 3, 10, 5, 7, 8, 9]))
print(slu.maxArea([9, 8, 7, 5, 10, 3, 2]))
