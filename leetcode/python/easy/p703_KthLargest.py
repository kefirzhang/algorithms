class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.helper = []
        if len(nums) > 0:
            nums.sort()
            self.helper = nums[-k:]

    def add(self, val: int) -> int:
        if len(self.helper) == 0:
            self.helper.append(val)
        else:
            if val >= self.helper[-1]:
                self.helper.append(val)
            elif val <= self.helper[0]:
                self.helper = [val] + self.helper
            else:
                i = 0
                while i < len(self.helper):
                    # if val == self.helper[i]:
                    # break
                    if val < self.helper[i]:
                        # print("#", i)
                        self.helper = self.helper[0:i] + [val] + self.helper[i:]
                        break
                    i += 1
        self.helper = self.helper[-self.k:]
        # print(self.helper)
        return self.helper[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [1,1])
print(obj.add(1))
print(obj.add(1))
print(obj.add(3))
print(obj.add(3))
print(obj.add(3))

print(obj.add(4))
print(obj.add(4))
print(obj.add(4))
'''
["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
45588
'''
