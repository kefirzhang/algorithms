class Solution:
    def isOneBitCharacter(self, bits):

        while len(bits) != 0:
            if bits[0] == 0 and len(bits) == 1:
                return True
            if bits[0] == 1 and len(bits) <= 2:
                return False

            if bits[0] == 0:
                bits.pop(0)
                continue
            if bits[0] == 1:
                bits.pop(0)
                bits.pop(0)
                continue
        return False


slu = Solution()
print(slu.isOneBitCharacter([1, 1, 1]))
