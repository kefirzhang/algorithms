class NumArray:
    def __init__(self, nums):
        length = len(nums)
        if length > 0:
            self.helper = [0] * len(nums)
            self.helper[0] = nums[0]
            for i in range(1, length):
                self.helper[i] = nums[i] + self.helper[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i - 1 < 0:
            return self.helper[j]
        else:
            return self.helper[j] - self.helper[i - 1]


# Your NumArray object will be instantiated and called as such:


# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

slu = NumArray([])
print(slu.sumRange(0, 2))

'''
["NumArray","sumRange","sumRange","sumRange"]
[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
'''
