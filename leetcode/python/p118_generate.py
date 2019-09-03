class Solution:
    def generate(self, numRows):
        l_data = []
        for i in range(1, numRows + 1):
            l_cur = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    l_cur.append(1)
                else:
                    l_cur.append(l_data[-1][j - 1] + l_data[-1][j])
            l_data.append(l_cur)
        return l_data


slu = Solution()
print(slu.generate(5))
