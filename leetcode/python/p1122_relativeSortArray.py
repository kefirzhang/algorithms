class Solution:
    def relativeSortArray(self, arr1, arr2):
        length = len(arr2)
        helper = [[]] * (length + 1)

        for i in arr1:
            if i in arr2:
                index = arr2.index(i)
            else:
                index = length
            helper[index] = helper[index] + [i]
        back = []

        helper[-1].sort()

        for arr in helper:
            back = back + arr

        return back
# 这个原来是搞计数排序的  声明arr2对应的数组 然后把出现的累加，没有出现的单方 最后拼接

slu = Solution()
print(slu.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
