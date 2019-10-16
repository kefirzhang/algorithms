class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()

        i, length = 0, len(arr)
        if length < 2:
            return []
        min_distance = arr[1] - arr[0]
        helper = []
        while i < length - 1:
            if arr[i + 1] - arr[i] == min_distance:
                helper.append([arr[i], arr[i + 1]])
            elif arr[i + 1] - arr[i] < min_distance:
                helper = []
                min_distance = arr[i + 1] - arr[i]
                helper.append([arr[i], arr[i + 1]])
            i += 1
        return helper


slu = Solution()
print(slu.minimumAbsDifference([4, 2, 1, 3]))
'''
[[1,2],[2,3],[3,4]]
'''
