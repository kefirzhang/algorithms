class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        helper = [0] * 61
        total = 0
        for i in time:
            helper[i % 60] += 1

        for i in range(1, 30):
            if helper[i] > 0:
                total += helper[i] * helper[60 - i]
        total += (helper[30] * (helper[30] - 1)) / 2
        total += (helper[0] * (helper[0] - 1)) / 2
        return int(total)


slu = Solution()
print(slu.numPairsDivisibleBy60([20, 20, 20, 40, 40, 40, 40, 40]))
