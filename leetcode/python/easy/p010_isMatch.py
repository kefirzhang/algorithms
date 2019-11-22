class Solution:
    def isMatch(self, s, p):
        p_lenth = len(p)
        for i,ch in enumerate(s):
            if s[i:p_lenth] == p:
                return True

        return False

solution = Solution()

print(solution.isMatch("abcdeft", 'ab'))
