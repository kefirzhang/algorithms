class Solution:
    def binaryGap(self, N: int) -> int:
        binstr = bin(N)
        arr = binstr[2:].split("1")[1:-1]
        ans = 0
        if len(arr) == 0:
            return ans

        for i in arr:
            ans = max(ans, len(i))

        return ans + 1


slu = Solution()
print(slu.binaryGap(8))
