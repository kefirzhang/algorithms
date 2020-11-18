# step 1 给出一块房间
# step 2 给出一个起始点
# step 3 开始扫描
import time

class Solution:
    def scan(self, room, y, x):
        m, n = len(room), len(room[0])
        # helperRoom = [[0 for _ in range(n)] for _ in range(m)]  # 标记
        route = []  # 记录的轨迹
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def helper(start_y, start_x):
            if room[start_y][start_x] == 1:
                return
            route.append([start_y, start_x])  # 扫描到当前点
            room[start_y][start_x] = 1  # 标记已经扫描过
            for direction in directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if new_x < 0 or new_x >= n - 1 or new_y < 0 or new_y >= m - 1:
                    continue
                helper(new_y, new_x)

        helper(y, x)
        print(room)
        for i, j in route:

            time.sleep(1)

        return route


room = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
slu = Solution()
slu.scan(room, 0, 0)
