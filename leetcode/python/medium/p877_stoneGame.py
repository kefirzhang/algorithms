class Solution:
    def stoneGame(self, piles) -> bool:
        total = sum(piles)

        def helper(pieces):
            if len(pieces) == 1:
                return pieces[0]
            return max(helper(pieces[:-1]) + pieces[-1], helper(pieces[1:]) + pieces[0])
        canGetMax = helper(piles)
        print(canGetMax)
        return True


slu = Solution()
print(slu.stoneGame([5, 3, 4, 5]))
