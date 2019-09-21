class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == "" and t == "":
            return True
        if len(s) != len(t):
            return False
        helper_map = {}
        helper_set = set()
        for i, n in enumerate(s):
            if helper_map.__contains__(n):
                if helper_map[n] != t[i]:
                    return False
            else:
                if t[i] in helper_set:
                    return False
                else:
                    helper_set.add(t[i])
                helper_map[n] = t[i]
        return True


slu = Solution()
print(slu.isIsomorphic("ab", "aa"))
