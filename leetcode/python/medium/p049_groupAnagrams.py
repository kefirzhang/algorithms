class Solution:
    def groupAnagrams(self, strs):
        helper = {}
        res = []
        for i in strs:
            tmp_key = list(i)
            tmp_key.sort()
            tmp_key = tuple(tmp_key)
            if helper.__contains__(tmp_key):
                helper[tmp_key].append(i)
            else:
                helper[tmp_key] = [i]

        for i in helper:
            res.append(helper[i])
        return res



slu = Solution()
print(slu.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
