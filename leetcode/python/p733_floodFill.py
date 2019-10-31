class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        helper = set()
        x_limit = len(image)
        y_limit = len(image[0])

        def doColor(x, y, color):
            helper.add((x, y))
            dots = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
            for dot in dots:
                if 0 <= dot[0] < x_limit and 0 <= dot[1] < y_limit and image[dot[0]][dot[1]] == image[x][y] and (
                dot[0], dot[1]) not in helper:
                    doColor(dot[0], dot[1], newColor)
            image[x][y] = color

        doColor(sr, sc, newColor)
        return image


slu = Solution()
print(slu.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
