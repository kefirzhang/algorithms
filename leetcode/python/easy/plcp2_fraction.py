class Solution:
    def fraction(self, cont):
        if len(cont) == 1:
            return [cont[0], 1]
        else:
            pre = self.fraction(cont[1:])
            up = pre[1] + pre[0] * cont[0]
            down = pre[0]
            # for i in range(2, up + 1):
            #     if up % i == 0 and down % i == 0:
            #         up = up / i
            #         down = down / i

            return [up, down]


slu = Solution()
print(slu.fraction([2,
                    7,
                    8,
                    6,
                    8,
                    7,
                    6,
                    5,
                    4, 4]))
