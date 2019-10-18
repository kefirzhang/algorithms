class Solution:
    def firstUniqChar(self, s: str) -> int:
        helper = {}
        for i in s:
            if helper.__contains__(i):
                helper[i] += 1
            else:
                helper[i] = 1
        for i, n in enumerate(s):
            if helper[n] == 1:
                return i

        return -1


slu = Solution()
print(slu.firstUniqChar("loveleetcode"))
