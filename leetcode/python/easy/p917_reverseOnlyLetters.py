class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        helper = list(S)

        def isW(s):
            return ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z')

        i, j = 0, len(S) - 1
        while i < j:
            if isW(S[i]) is False:
                i += 1
                continue
            if isW(S[j]) is False:
                j -= 1
                continue
            helper[i], helper[j] = helper[j], helper[i]
            i += 1
            j -= 1
        return "".join(helper)


slu = Solution()
print(slu.reverseOnlyLetters("ab-cd"))
