class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


slu = Solution()
print(slu.canWinNim(5))

