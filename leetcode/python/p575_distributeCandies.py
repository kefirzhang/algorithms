class Solution:
    def distributeCandies(self, candies):
        middle = int(len(candies) / 2)
        diff = len(set(candies))
        return middle if diff > middle else diff


slu = Solution()
print(slu.distributeCandies([1, 1, 1, 1, 1, 1, 1, 1]))
