# 简洁的代码确实有一种美感
class Solution:
    def combine(self, n: int, k: int):
        def backtrace(first=1, arr=[]):
            if len(arr) == k:
                output.append(arr[:])
                return
            for i in range(first, n + 1):
                arr.append(i)
                backtrace(i + 1, arr)
                arr.pop()
            return arr

        output = []
        backtrace()
        return output


slu = Solution()
print(slu.combine(5, 5))
