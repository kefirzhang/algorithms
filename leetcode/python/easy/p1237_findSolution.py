# This is the custom function interface.
# You should not implement it, or speculate about its implementation
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y


class Solution:
    def findSolution(self, customfunction, z: int):
        ret = []
        i = 1
        while customfunction.f(i, 1) <= z:
            j = 1
            while True:
                if customfunction.f(i, j) == z:
                    ret.append([i, j])
                    break
                elif customfunction.f(i, j) > z:
                    break
                else:
                    j += 1
            i += 1

        return ret


cf = CustomFunction()
slu = Solution()
print(slu.findSolution(CustomFunction(), 5))
