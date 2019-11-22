class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if 0 <= x < 10:
            return True
        if x%10 == 0:
            return False

        recv = 0
        while recv < x:
            p = x % 10
            x = int(x / 10)
            recv = recv * 10 + p

        if x == recv:
            return True

        if int(recv / 10) == x and x != 0:
            return True

        return False


solution = Solution()
print(solution.isPalindrome(2112))
