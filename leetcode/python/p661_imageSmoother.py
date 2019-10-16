class Solution:
    def imageSmoother(self, M):
        x_length = len(M[0])
        y_length = len(M)
        new_m = []
        for x in range(y_length):
            new_m.append([0] * x_length)

        for i, record in enumerate(M):
            for j, n in enumerate(record):
                dots = set([(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1),
                            (i + 1, j + 1), (i + 1, j - 1), (i, j)])
                cur_dots_num = 0
                cur_dots_total = 0
                for dot in dots:
                    if 0 <= dot[0] < y_length and 0 <= dot[1] < x_length:
                        cur_dots_num += 1
                        cur_dots_total += M[dot[0]][dot[1]]

                new_m[i][j] = int(cur_dots_total / cur_dots_num)
                # print(new_m)
        return new_m


slu = Solution()
print(slu.imageSmoother([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]))

# print([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]][1])


'''
[
[2, 3, 4], 
[5, 6, 7], 
[8, 9, 10], 
[11, 12, 13], 
[14, 15, 16]]

输出
[
[4,4,5],
[6,6,6],
[8,9,9],
[11,11,12],
[12,12,12]
]
正确
[
[4,4,5],
[5,6,6],
[8,9,9],
[11,12,12],
[13,13,14]]
'''
