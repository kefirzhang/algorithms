class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        indegrees = [0 for _ in range(numCourses)]  # 某一个课程依赖多少个
        adjacency = [[] for _ in range(numCourses)]  # 某一个课程被依赖的课程列表
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            pre = queue.pop()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses


slu = Solution()
print(slu.canFinish(2, [[1, 0],[0,1]]))
