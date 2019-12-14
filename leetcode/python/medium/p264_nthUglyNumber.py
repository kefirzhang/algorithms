class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        heap = [1]
        heapq.heapify(heap)
        for _ in range(n):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:
                heapq.heappop(heap)
            a, b, c = res * 2, res * 3, res * 5
            heapq.heappush(heap, a)
            heapq.heappush(heap, b)
            heapq.heappush(heap, c)

        return res

    def nthUglyNumber2(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        n_2, n_3, n_5 = 0, 0, 0
        for i in range(1, n):
            minnum = min(dp[n_2] * 2, dp[n_3] * 3, dp[n_5] * 5)
            dp[i] = minnum

            if minnum == dp[n_2] * 2:
                n_2 += 1
            if minnum == dp[n_3] * 3:
                n_3 += 1
            if minnum == dp[n_5] * 5:
                n_5 += 1
            # print(minnum, n_2, n_3, n_5)
        return dp[-1]


slu = Solution()
print(slu.nthUglyNumber2(10))
