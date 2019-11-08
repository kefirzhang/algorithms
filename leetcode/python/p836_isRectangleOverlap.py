class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        # x1 y1 x2 y2
        # x1y1 x1y2 x2y1 x2y2
        #
        # 左下 x1y1  右上 x2y2 左上 x1y2 右下 x2y1
        if (
                (rec1[2] <= rec2[0]) or
                (rec1[0] >= rec2[2]) or
                (rec1[1] >= rec2[3]) or
                (rec1[3] <= rec2[1])

        ):
            return False

        return True
    def isRectangleOverlap3(self, rec1, rec2) -> bool:  #这些是错的示范
        # x1 y1 x2 y2
        # x1y1 x1y2 x2y1 x2y2
        # 左下 大于 右上 or 右上 小于 左下 or 左上 小于 右下 or 右下 大于 坐上
        # 左下 x1y1  右上 x2y2 左上 x1y2 右下 x2y1
        if (
                (rec1[0] >= rec2[2] and rec1[1] >= rec2[3]) or
                (rec1[2] <= rec2[0] and rec1[3] <= rec2[1]) or
                (rec1[0] <= rec2[2] and rec1[3] > rec2[1]) or
                (rec1[2] >= rec2[0] and rec1[1] < rec2[3])

        ):
            return False

        return True
    # 这个逻辑有问题
    def isRectangleOverlap2(self, rec1, rec2) -> bool: #这些是错的示范
        # x1 y1 x2 y2
        # x1y1 x1y2 x2y1 x2y2
        # ab x1 < a < x2   y1 < b < y2
        if (
                (rec2[0] < rec1[0] < rec2[2] and rec2[1] < rec1[1] < rec2[3]) or
                (rec2[0] < rec1[0] < rec2[2] and rec2[1] < rec1[3] < rec2[3]) or
                (rec2[0] < rec1[2] < rec2[2] and rec2[1] < rec1[1] < rec2[3]) or
                (rec2[0] < rec1[2] < rec2[2] and rec2[1] < rec1[3] < rec2[3])
        ):
            return True

        return False


slu = Solution()
print(slu.isRectangleOverlap([0,0,1,1], [1,0,2,1]))
