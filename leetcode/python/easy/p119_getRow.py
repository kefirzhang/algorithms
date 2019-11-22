class Solution:
    def getRow(self, numRows):  # 进阶到O(K)空间复杂度核心点是扩充上一个数组
        l_data = [1]
        if numRows == 0:
            return [1]
        for i in range(numRows):
            for j in range(i + 1):
                if j != i:
                    l_data[j] = l_data[j] + l_data[j + 1]
            l_data = [1] + l_data

        return l_data

    def getRow1(self, numRows):
        numRows += 1
        l_data = []
        for i in range(1, numRows + 1):
            l_cur = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    l_cur.append(1)
                else:
                    l_cur.append(l_data[-1][j - 1] + l_data[-1][j])
            l_data.append(l_cur)
        return l_data[-1]


slu = Solution()
print(slu.getRow(4))
