class Solution:
    def addToArrayForm(self, A, K):
        helper = []
        num_a = 0
        carry = 0
        while len(A) > 0:
            num_a = num_a + A.pop() * (10 ** carry)
            carry += 1
        num = num_a + K
        while num > 0:
            addons = num % 10
            num = int(num / 10)
            helper.insert(0, addons)
        return helper


slu = Solution()
print(slu.addToArrayForm([1, 2, 0, 1], 34))
