class Solution:
    def powerfulIntegers(self, x, y, bound):
        helper = []
        helper_x = set()
        helper_y = set()

        if x == 1:
            helper_x.add(1)
        else:
            i = 0
            while x ** i < bound:
                helper_x.add(x ** i)
                i += 1

        if y == 1:
            helper_y.add(1)
        else:
            j = 0
            while y ** j < bound:
                helper_y.add(y ** j)
                j += 1

        for k in range(1, bound + 1):
            for l in helper_x:
                if k - l in helper_y:
                    if k not in helper:
                        helper.append(k)
        return helper


slu = Solution()
print(slu.powerfulIntegers(2, 1, 10))
