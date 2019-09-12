class Solution:
    def wordPattern(self, pattern, s) -> bool:
        helper_list = s.split(" ")
        helper_map = {}
        helper_set = set()
        if len(pattern) != len(helper_list):
            return False

        for i, n in enumerate(pattern):
            if helper_map.__contains__(n):
                if helper_list[i] != helper_map[n]:
                    return False
            else:
                if helper_list[i] in helper_set:
                    return False
                else:
                    helper_set.add(helper_list[i])
                helper_map[n] = helper_list[i]

        return True


slu = Solution()
print(slu.wordPattern("abba", "dog dog dog dog"))
