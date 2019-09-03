class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        length = len(s)
        if length == 0:
            return True
        i = 0
        j = length - 1
        while i < j:
            if not ('a' <= s[i] <= 'z' or "0" <= s[i] <= "9"):
                i += 1
                continue
            if not ('a' <= s[j] <= 'z' or "0" <= s[j] <= "9"):
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


slu = Solution()
print(slu.isPalindrome("aa"))
