class Solution:
    def gardenNoAdj(self, N, paths):
        helper = {}
        for path in paths:
            if helper.__contains__(path[0]):
                helper[path[0]].append(path[1])
            else:
                helper[path[0]] = [path[1]]
            if helper.__contains__(path[1]):
                helper[path[1]].append(path[0])
            else:
                helper[path[1]] = [path[0]]
        garden = [0] * (N + 1)  # 花园
        for i in range(1, N + 1):  # 遍历花园
            selection = [1, 2, 3, 4]  # 可以种植的花的选择
            if helper.__contains__(i):
                for friend in helper[i]:  # 所有的路径 交集
                    if garden[friend] != 0 and garden[friend] in selection:
                        selection.remove(garden[friend])
            garden[i] = selection[0]
        return garden[1:]


slu = Solution()
print(slu.gardenNoAdj(10000, [[1,2]]))
