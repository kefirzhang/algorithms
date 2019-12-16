class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        helper = {}
        for i, j in prerequisites:
            if helper.__contains__(j):
                helper[j] += 1
            else:
                helper[j] = 1
        return helper
        return True


slu = Solution()
print(slu.canFinish(2, [[1, 0]]))
