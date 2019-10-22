class Solution:
    def isBoomerang(self, points) -> bool:
        if points[2][0] == points[1][0] and points[2][1] == points[1][1]:
            return False
        if points[1][0] == points[0][0] and points[1][1] == points[0][1]:
            return False

        if (points[2][0] - points[0][0]) * (points[1][1] - points[0][1]) == (points[1][0] - points[0][0]) * (
                points[2][1] - points[0][1]):
            return False

        return True


slu = Solution()
print(slu.isBoomerang([[1, 1], [2, 3], [3, 2]]))
