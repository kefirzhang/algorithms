class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        helper = list(s)
        for i in range(0, len(helper), 2 * k):
            helper[i:i + k] = reversed(helper[i:i + k])

        return "".join(helper)


slu = Solution()
print(slu.reverseStr("abcdefg", 2))
