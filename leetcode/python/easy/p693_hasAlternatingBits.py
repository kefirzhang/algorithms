class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n > 0:
            cur = n & 1
            n = n >> 1
            if n > 0:
                after = n & 1
                if cur == after:
                    return False
            else:
                break

        return True


slu = Solution()
print(slu.hasAlternatingBits(10))
