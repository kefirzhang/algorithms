class Solution:
    def lengthOfLastWord(self, s):
        l = len(s) - 1
        num = 0
        while l >= 0:
            if s[l] == " " and num == 0:
                l -= 1
                continue
            if s[l] == " ":
                return num
            else:
                num += 1
            l -= 1
        return num


slu = Solution()
print(slu.lengthOfLastWord("a "));
