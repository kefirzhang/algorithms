class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for i, n in enumerate(s):
            if n in t:
                t.remove(n)
            else:
                return n
        return t[0]


slu = Solution()
print(slu.findTheDifference("ae", "aea"))
