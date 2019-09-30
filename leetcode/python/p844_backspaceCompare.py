class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = ""
        t = ""
        for i in S:
            if i == "#":
                s = s[:-1]
            else:
                s = s + i
        for j in T:
            if j == "#":
                t = t[:-1]
            else:
                t = t + j
        return s == t


slu = Solution()
print(slu.backspaceCompare("ab#c", "ad#c"))
