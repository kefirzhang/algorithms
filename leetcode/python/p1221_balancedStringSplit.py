class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right, total = 0, 0, 0

        for i in s:
            if i == 'R':
                right += 1
            else:
                left += 1

            if left == right and left != 0:
                total += 1
                left, right = 0, 0

        return total


slu = Solution()
print(slu.balancedStringSplit("RLRRLLRLRL"))
