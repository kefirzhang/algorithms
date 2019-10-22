class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        num_package = [0] * num_people
        step = 1
        while candies > 0:
            num_package[((step - 1) % num_people)] += step if candies > step else candies
            candies -= step
            step += 1

        return num_package


slu = Solution()
print(slu.distributeCandies(7, 4))
