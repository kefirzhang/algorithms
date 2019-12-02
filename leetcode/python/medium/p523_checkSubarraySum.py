class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        hashMap = {0: -1}
        sum_num = 0
        for i, n in enumerate(nums):
            sum_num += n
            if k != 0:
                sum_num = sum_num % k
            if hashMap.__contains__(sum_num):
                if i - hashMap[sum_num] >= 1:
                    return True
            else:
                hashMap[sum_num] = i
        print(hashMap)
        return False

    def checkSubarraySum2(self, nums, k: int) -> bool:
        m = len(nums)
        dp = [[0] * m for i in range(m)]

        for i, n in enumerate(nums):
            if i == 0:
                dp[0][i] = n
            else:
                dp[0][i] = n + dp[0][i - 1]
                if k == 0 and dp[0][i] == 0:
                    return True
                elif k != 0 and dp[0][i] % k == 0:
                    return True
        return dp[0]
        for i in range(1, m):
            for j in range(m - 1, i, -1):
                dp[i][j] = dp[0][j] - dp[0][i - 1]
                if dp[i][j] != 0 and dp[i][j] < k:
                    break
                if k == 0 and dp[i][j] == 0:
                    return True
                elif k != 0 and dp[i][j] % k == 0:
                    return True
        return False


slu = Solution()
print(slu.checkSubarraySum([0, 1, 0], 0))
