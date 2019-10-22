class Solution:
    def robotSim(self, commands, obstacles) -> int:
        p_x, p_y, d_p = 0, 0, 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        dots = set(map(tuple, obstacles))
        ans = 0
        for i in commands:
            if i == -1:  # 右转
                d_p = (d_p + 1) % 4
            elif i == -2:  # 左转
                d_p = (d_p + 3) % 4
            else:
                for j in range(i):
                    if (p_x + dx[d_p], p_y + dy[d_p]) not in dots:
                        p_x += dx[d_p]
                        p_y += dy[d_p]
                        ans = max(ans, p_x * p_x + p_y * p_y)
        return ans


slu = Solution()
print(slu.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
