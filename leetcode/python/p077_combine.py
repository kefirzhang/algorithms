class Solution:

    def combine(self, n, k):
        if k > n or n == 0:
            return []
        if n == k:
            return [list(range(1, n + 1))]
        res = []
        self.find_combine(1, n, k, [], res)
        return res

    def find_combine(self, start, n, k, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return
        for i in range(start, n + 1):
            pre.append(i)
            self.find_combine(i + 1, n, k, pre, res)
            pre.pop()


slu = Solution()
print(slu.combine(2, 1))
