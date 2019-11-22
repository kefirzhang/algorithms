class Solution:
    def repeatedNTimes(self, A) -> int:
        helper = set()
        for i in A:
            if i in helper:
                return i
            else:
                helper.add(i)


slu = Solution()
print(slu.repeatedNTimes([2, 1, 2, 5, 3, 2]))
