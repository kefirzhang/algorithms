class Solution:
    def reverseString(self, s) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        """
        Do not return anything, modify s in-place instead.
        """
        # print(s)


slu = Solution()
print(slu.reverseString(["h", "e", "l", "l", "o"]))
