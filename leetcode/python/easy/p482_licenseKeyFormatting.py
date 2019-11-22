class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = list(S.replace("-", "").upper())
        i = len(S)
        ret = []
        while i > 0:
            start = i - K
            end = i
            start = start if start >= 0 else 0
            str = S[start:end]
            if len(str) > 0:
                ret.insert(0, "".join(str))
                # ret.append("".join(str))
            i -= K
        return "-".join(ret)


slu = Solution()
print(slu.licenseKeyFormatting("2-5g-3-J",2))
