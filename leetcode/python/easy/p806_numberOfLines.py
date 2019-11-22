class Solution:
    def numberOfLines(self, widths, S):
        per_line = 0
        ans_line = 1
        for i in S:
            width = widths[ord(i) - ord('a')]

            if per_line + width > 100:
                ans_line += 1
                per_line = width
            else:
                per_line += width
            # print(per_line,i,width)
        return [ans_line, per_line]


slu = Solution()
print(slu.numberOfLines(
    [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    , "bbbcccdddaaa"))
