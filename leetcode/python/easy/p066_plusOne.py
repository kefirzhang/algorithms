class Solution:
    def plusOne(self, digits):
        length = len(digits) - 1
        carry = 1
        while length >= 0:
            digits[length] += carry
            if digits[length] >= 10:
                digits[length] -= 10
                carry = 1
            else:
                carry = 0
            length -= 1

        if carry > 0:
            digits = [1] + digits

        return digits


slu = Solution()
print(slu.plusOne([0]))
