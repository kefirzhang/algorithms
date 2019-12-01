class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        s = "0" + s
        dp = [0] * (length + 1)

        for i in range(1, length + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, 0, -1):
                middle = int((i + j) / 2)
                if (i - j) % 2 == 0:  # 奇数长度 有中心点对称
                    # print(i, j, middle, s[j:middle], s[middle + 1:i + 1], "even")
                    if s[j:middle] == s[middle + 1:i + 1][::-1]:
                        # print(s[j:i+1])
                        dp[i] += 1
                else:
                    # print(i, j, middle, s[j:middle + 1], s[middle + 1:i + 1], "odd")
                    if s[j:middle + 1] == s[middle + 1:i + 1][::-1]:
                        dp[i] += 1
                        print(s[j:i + 1])

        # print(dp)
        return dp[-1]


slu = Solution()
print(slu.countSubstrings("dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"))
