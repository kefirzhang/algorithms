# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
class Solution:
    def convert(self, string, numRows):
        if numRows <= 1:
            return string
        numList = []
        for i in range(numRows):
            numList.append([])

        direction = False
        rowListIndex = 0
        idx = 0
        while idx < len(string):

            numList[rowListIndex].append(string[idx])

            if idx % (numRows - 1) == 0:
                if direction == 1:
                    direction = -1
                else:
                    direction = 1
            rowListIndex += direction

            idx += 1
        backstr = ""
        for i in range(numRows):
            backstr = backstr + "".join(numList[i])

        return backstr


solution = Solution()
print(solution.convert("a", 2))
