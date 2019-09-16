class Solution:
    def thirdMax(self, nums):
        INI_MIN = -2 ** 31
        helper = []
        for n in nums:
            if n in helper:
                continue
            elif len(helper) == 0:
                helper.append(n)
                continue
            else:
                if len(helper) < 3:
                    helper.append(INI_MIN)
                for i_i, i_n in enumerate(helper):
                    if n > i_n:
                        helper = helper[0:i_i] + [n] + helper[i_i:]
                        helper.pop()
                        print(helper)
                        break
        if len(helper) == 3:
            return helper[-1]
        else:
            return helper[0]


slu = Solution()
print(slu.thirdMax([1, 2, 3, 4, 5, 5, 5, 5, 5]))
