class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sArr, pArr = list(s), list(p)
        lenS, lenP = len(s), len(p)
        dp = [[False] * (lenS + 1) for i in range(lenP + 1)]
        dp[0][0] = True
        for i in range(1, lenP + 1):
            if pArr[i - 1] != "*":
                break
            else:
                dp[i][0] = True

        for i in range(1, lenP + 1):
            for j in range(1, lenS + 1):
                if sArr[j - 1] == pArr[i - 1] or pArr[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pArr[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[lenP][lenS]


slu = Solution()
print(slu.isMatch("ab", ".*"))
