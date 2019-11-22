import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


slu = Solution()
print(slu.bulbSwitch(102))
