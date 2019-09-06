class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t) or len(s) == 0 or len(t) == 0:
            return False
        pre_map = {}
        for i in s:
            if pre_map.__contains__(i):
                pre_map[i] += 1
            else:
                pre_map[i] = 1
        for j in t:
            if not pre_map.__contains__(j):
                return False
            pre_map[j] -= 1
            if pre_map[j] == 0:
                del pre_map[j]
        if len(pre_map) == 0:
            return True
        else:
            return False


slu = Solution()
print(slu.isAnagram("anagram", "nagaram"))
