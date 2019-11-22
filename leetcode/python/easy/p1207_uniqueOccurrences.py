class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        helper = {}

        for i in arr:
            if helper.__contains__(i):
                helper[i] += 1
            else:
                helper[i] = 1
        times = set()
        for i in helper:
            if helper[i] in times:
                return False
            else:
                times.add(helper[i])

        return True


slu = Solution()
print(slu.uniqueOccurrences([1, 5, 2, 1, 1, 3]))
