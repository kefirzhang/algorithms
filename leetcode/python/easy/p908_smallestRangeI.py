class Solution:
    def smallestRangeI(self, A, K: int) -> int:
        A.sort()
        distance = A[-1] - A[0]
        if distance > 2*K:
            return distance - 2*K
        else:
            return 0


slu = Solution()
print(slu.smallestRangeI([1, 3, 6],3))
