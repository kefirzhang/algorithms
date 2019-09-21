class Solution:
    def toLowerCase(self, s):
        helper = ''
        for i in s:
            if ord('A') <= ord(i) <= ord('Z'):
                helper += chr(ord(i) + 32)
            else:
                helper += i
        return helper


slu = Solution()
print(slu.toLowerCase("HelloZ"))
