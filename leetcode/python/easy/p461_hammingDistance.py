class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = x ^ y
        return str(bin(c)).count("1")


slu = Solution()
print(slu.hammingDistance(10, 20))
