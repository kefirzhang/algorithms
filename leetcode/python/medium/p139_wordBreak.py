class Solution:
    def wordBreak2(self, s: str, wordDict) -> bool:
        if s == "":
            return True
        for word in wordDict:
            if word in s:
                tmp_s = s.replace(word, "")
                if self.wordBreak(tmp_s, wordDict):
                    return True
        return False

    def wordBreak3(self, s: str, wordDict) -> bool:
        if s == "":
            return True
        for word in wordDict:
            if word == s[0:len(word)]:
                if self.wordBreak(s[len(word):], wordDict):
                    return True
        return False

    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


slu = Solution()
print(slu.wordBreak("leetcode", ["leet", "code"]))
