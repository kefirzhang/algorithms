class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            stones.sort()

            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                new_stone = stones[-1] - stones[-2]
                stones = stones[:-2]
                stones.append(new_stone)
        if len(stones) > 0:
            return stones[0]
        return 0


slu = Solution()
print(slu.lastStoneWeight([1, 2, 3, 4, 5, 6, 7]))
