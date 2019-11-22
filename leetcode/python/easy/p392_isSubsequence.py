class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        j = 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
            j += 1

        return False


slu = Solution()
print(slu.isSubsequence("", "ahbgdc"))
