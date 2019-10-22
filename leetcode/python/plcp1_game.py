class Solution:
    def game(self, guess, answer) -> int:
        helper = 0
        for i, n in enumerate(guess):
            if n == answer[i]:
                helper += 1
        return helper


slu = Solution()
print(slu.game([1, 2, 3], [1, 2, 3]))
