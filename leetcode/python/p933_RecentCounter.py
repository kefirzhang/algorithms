class RecentCounter:

    def __init__(self):
        self.helper = []

    def ping(self, t: int) -> int:
        self.helper.append(t)

        if self.helper[-1] - self.helper[0] > 3000:
            i = 0
            while i < len(self.helper):

                if self.helper[-1] - self.helper[i] <= 3000:
                    print(i)
                    self.helper = self.helper[i:]
                    break
                i += 1
        return len(self.helper)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)

param_4 = obj.ping(3002)
print(param_1, param_2, param_3, param_4)
