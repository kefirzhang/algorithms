class Solution:
    def __init__(self):
        self.helper = {}

    def isHappy(self, n):
        if self.helper.__contains__(n):
            return False
        else:
            self.helper[n] = n

        sum = 0
        while n >= 10:
            sum += pow(n % 10, 2)
            n = int(n / 10)
        sum += pow(n, 2)
        if sum == 1:
            return True
        else:
            return self.isHappy(sum)


slu = Solution()
print(slu.isHappy(3))
