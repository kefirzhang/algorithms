class MinStack:

    def __init__(self):
        self.data = []  # 栈数组
        self.helper = []  # 辅助函数 一一对应

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        self.data.pop()
        self.helper.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self):
        return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(10)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)
