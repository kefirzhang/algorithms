class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        def dfs(x, y):
            if x not in graph:
                return -1
            if x == y:
                return 1
            for node in graph[x]:
                if node == y:
                    return graph[x][node]
                elif node not in visited:
                    visited.add(node)
                    t = dfs(node, y)
                    if t != -1:
                        return graph[x][node] * t

            return -1

        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res


slu = Solution()
print(slu.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                       [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
