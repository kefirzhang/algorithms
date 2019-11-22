class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates) <= 2:
            return True
        dot1 = coordinates[0]
        dot2 = coordinates[1]

        for i in range(2, len(coordinates)):
            dot3 = coordinates[i]
            if (dot3[1] - dot1[1]) * (dot2[0] - dot1[0]) - (dot2[1] - dot1[1]) * (dot3[0] - dot1[0]) != 0:
                return False

        return True


slu = Solution()
print(slu.checkStraightLine([[1, 1], [2, 2], [3, 3]]))
