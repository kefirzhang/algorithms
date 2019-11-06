class Solution:
    def diStringMatch(self, S: str):
        l = 0
        r = len(S)
        ret = []
        for i in S:
            if i == "I":
                ret.append(l)
                l += 1
            else:
                ret.append(r)
                r -= 1
        ret.append(r)
        return ret


slu = Solution()
print(slu.diStringMatch("III"))
