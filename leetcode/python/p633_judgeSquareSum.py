class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        helper = set()
        i = 0
        while i * i <= c:
            helper.add(i * i)
            i += 1
        j = 0
        while j * j <= c:
            if (c - j * j) in helper:
                return True
            j += 1
        return False


slu = Solution()

print(slu.judgeSquareSum(4))
