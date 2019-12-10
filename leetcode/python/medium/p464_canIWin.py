class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        unused = {}
        for i in range(1, maxChoosableInteger + 1):
            unused[i] = True

        return self.helper(unused, desiredTotal)

    def helper(self, unused, desiredTotal):

        for i in unused:

            self.helper()

            print(i, unused[i])

            del used[i]
        return True


slu = Solution()
print(slu.canIWin(10, 11))
