class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        common = strs[0]
        for s_str in strs:
            tmp_common = ""
            min_len = min(len(common), len(s_str))
            for idx in range(min_len):
                if common[idx] == s_str[idx]:
                    tmp_common += s_str[idx]
                else:
                    break
            common = tmp_common
            if common == "":
                return ""
        return common


slu = Solution()
print(slu.longestCommonPrefix(["aca","cba"]))
