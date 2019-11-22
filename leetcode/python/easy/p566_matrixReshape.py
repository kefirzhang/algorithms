class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        helper = []
        ret = []
        for i in nums:
            helper += i[:]
        if r * c != len(helper):
            return nums

        j = 0
        for m in range(r):
            record = []
            for n in range(c):
                record.append(helper[j])
                j += 1
            ret.append(record)
        return ret


slu = Solution()
print(slu.matrixReshape([[1,2],[3,4]], 4, 1))

'''
[[1,2],[3,4]]
4
1
'''