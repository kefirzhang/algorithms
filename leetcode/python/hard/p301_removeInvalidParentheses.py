class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(s):
            l, r = 0, 0
            for i in s:
                if i == '(':
                    l += 1
                elif i == ")":
                    if l > 0:
                        l -= 1
                    else:
                        return False
            return l == 0

        def dfs(s, start, l, r):
            if l == 0 and r == 0 and is_valid(s):
                ans.append(s)
            for i in range(start, len(s)):
                if i - 1 >= start and s[i] == s[i - 1]:
                    continue
                elif s[i] == "(" and l > 0:
                    dfs(s[:i] + s[i + 1:], i, l - 1, r)
                elif s[i] == ")" and r > 0:
                    dfs(s[:i] + s[i + 1:], i, l, r - 1)

        ans = []
        l, r = 0, 0
        for i in s:
            if i == "(":
                l += 1
            elif i == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1
        dfs(s, 0, l, r)
        return ans


slu = Solution()
print(slu.removeInvalidParentheses("()())()"))
