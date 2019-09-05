class Solution:
    def countPrimes(self, n):
        helper = [1] * n
        if n < 3:
            return 0
        helper[0] = 0
        helper[1] = 0
        idx = 2
        while idx < n:
            if helper[idx] == 0:
                idx += 1
                continue

            i_idx = idx + idx
            while i_idx < n:
                helper[i_idx] = 0
                i_idx += idx
            idx += 1
        return sum(helper)


slu = Solution()
print(slu.countPrimes(64))
