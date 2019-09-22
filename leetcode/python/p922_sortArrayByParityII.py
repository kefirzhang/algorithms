class Solution:
    def sortArrayByParityII(self, A):
        helper_odd = []
        helper_even = []
        helper = []
        for i in A:
            if i % 2 == 0:
                helper_even.append(i)
            else:
                helper_odd.append(i)
        for i, n in enumerate(helper_even):
            helper.append(n)
            helper.append(helper_odd[i])
        return helper


slu = Solution()
print(slu.sortArrayByParityII([4, 2, 5, 7]))
