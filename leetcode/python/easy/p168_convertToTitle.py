import  math
class Solution:
    def convertToTitle(self, n):
        s = '#ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        back = ''
        while n >= 26:
            idx = n%26
            n = int(n / 26)
            if idx == 0:
                n -= 1
                back = s[-1] + back
            else:
                back = s[idx] + back
        if n != 0:
            back = s[n] + back
        return back


slu = Solution()
print(slu.convertToTitle(676))
