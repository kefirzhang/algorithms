class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                a = s[i + 1: j + 1]
                b = s[i:j]
                return a[::-1] == a or b[::-1] == b
            i += 1
            j -= 1

        return True


slu = Solution()
print(slu.validPalindrome("abca"))
