class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        ans += min(prev, cur)
        return ans

    def countBinarySubstrings3(self, s: str) -> int:
        group = [1]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                group.append(1)
            else:
                group[-1] = group[-1] + 1
        ans = 0
        # print(group)
        for i in range(1, len(group)):
            ans += min(group[i], group[i - 1])

        return ans

    def countBinarySubstrings2(self, s: str) -> int:
        helper = []
        i, j = 0, 0
        while i < len(s) - 1:
            j = i + 1
            while j < len(s):
                if s[j] != s[j - 1] and s[j] in s[i:j]:
                    break

                if s[i:j + 1].count("0") == s[i:j + 1].count("1"):
                    helper.append(s[i:j + 1])
                    break
                j += 1
            i += 1
        # print(helper)
        return len(helper)


slu = Solution()
print(slu.countBinarySubstrings("000111000"))
