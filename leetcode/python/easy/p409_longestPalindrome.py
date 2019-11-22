class Solution:
    def longestPalindrome(self, s: str) -> int:
        helper = {}
        for i in s:
            if helper.__contains__(i):
                helper[i] += 1
            else:
                helper[i] = 1
        print(helper)
        odd = False
        max_length = 0
        for i in helper:
            if helper[i] % 2 == 0:
                max_length += helper[i]
            else:
                odd = True
                max_length += helper[i] - 1
        if odd:
            max_length += 1
        return max_length


slu = Solution()
print(slu.longestPalindrome("bb"))
