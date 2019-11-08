class Solution:
    def largestTriangleArea(self, points) -> float:
        length = len(points)

        def area(p, q, r):
            return .5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1]
                            - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])

        max_area = 0
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if i != j and i != k and j != k:
                        max_area = max(max_area, area(points[i], points[j], points[k]))
        return max_area


slu = Solution()
print(slu.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
