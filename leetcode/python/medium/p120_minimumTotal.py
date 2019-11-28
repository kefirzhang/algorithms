class Solution:
    def minimumTotal(self, triangle) -> int:
        length = len(triangle)
        length -= 2
        while length >= 0:
            for i, n in enumerate(triangle[length]):
                triangle[length][i] = n + min(triangle[length + 1][i], triangle[length + 1][i + 1])
            length -= 1

        return triangle[0][0]


slu = Solution()
print(slu.minimumTotal([[2],
                        [3, 4],
                        [6, 5, 7],
                        [4, 1, 8, 3]
                        ]))
