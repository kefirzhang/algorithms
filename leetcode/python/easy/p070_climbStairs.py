class Solution:
    l = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n in self.l:
            return self.l[n]
        self.l[n - 1] = self.climbStairs(n - 1)
        self.l[n - 2] = self.climbStairs(n - 2)
        return self.l[n - 1] + self.l[n - 2]


slu = Solution()
print(slu.climbStairs(4))
