class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        nlen = len(s)
        for i in range(nlen):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, left * 2)

            if right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(nlen - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, left * 2)

            if right < left:
                left, right = 0, 0

        return max_length
slu = Solution()
print(slu.longestValidParentheses(")()())"))
