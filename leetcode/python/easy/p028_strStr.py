class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        length = len(haystack)
        n_length = len(needle)
        for i, n in enumerate(haystack):
            if i + n_length > length:
                return -1
            if haystack[i:i + n_length] == needle:
                return i
        return -1


slu = Solution()
print(slu.strStr("baaa", "aa"))
