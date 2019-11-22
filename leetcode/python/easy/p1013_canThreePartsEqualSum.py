class Solution:
    def canThreePartsEqualSum(self, A):
        the_num = int(sum(A) / 3)
        for i in range(3):
            carry = the_num
            while carry != 0 and len(A) > 0:
                carry = carry - A.pop()

        if carry != 0 or sum(A) != 0:
            return False
        else:
            return True


slu = Solution()
print(slu.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
