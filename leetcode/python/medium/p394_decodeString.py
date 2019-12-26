class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s, i):
            res, multi = "", 0
            while i < len(s):
                if s[i] == "[":
                    i, tmp = helper(s, i + 1)
                    res = res + multi * tmp
                    multi = 0
                elif s[i] == "]":
                    return i,res
                elif "0" <= s[i] <= "9":
                    multi = multi * 10 + int(s[i])
                else:
                    res += s[i]
                i += 1
            return res

        return helper(s, 0)


slu = Solution()
print(slu.decodeString("3[a2[c]]"))
