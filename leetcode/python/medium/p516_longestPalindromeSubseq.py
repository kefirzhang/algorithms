class Solution:


    def longestPalindromeSubseqxxx(self, s: str) -> int: # 这个是子序列 不是子字符串
        # 下面的解法是没搞懂题目
        length = len(s)
        max_long = 0
        for i in range(length):
            print(i)
            even_long = 0
            m, n = i, i + 1
            while m >= 0 and n < length and s[m] == s[n]:
                even_long += 2
                m -= 1
                n += 1

            odd_long = 1
            m, n = i - 1, i + 1
            while m >= 0 and n < length and s[m] == s[n]:
                odd_long += 2
                m -= 1
                n += 1
            max_long = max(max_long, even_long, odd_long)

        return max_long


slu = Solution()
print(slu.longestPalindromeSubseq("bbbab"))
