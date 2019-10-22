class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        num, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                num += 1
                i += 1
                j += 1
            else:
                j += 1

        return num


slu = Solution()
print(slu.findContentChildren([1, 2], [1, 2, 3]))
