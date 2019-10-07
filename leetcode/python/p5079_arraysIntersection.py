class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        helper_combine = {}
        for i in arr1:
            if helper_combine.__contains__(i):
                helper_combine[i] += 1
            else:
                helper_combine[i] = 1
        for i in arr2:
            if helper_combine.__contains__(i):
                helper_combine[i] += 1
            else:
                helper_combine[i] = 1
        for i in arr3:
            if helper_combine.__contains__(i):
                helper_combine[i] += 1
            else:
                helper_combine[i] = 1

        helper = []
        for j in helper_combine:
            if helper_combine[j] == 3:
                helper.append(j)

        return helper


slu = Solution()
print(slu.arraysIntersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]))
