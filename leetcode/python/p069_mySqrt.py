class Solution:
    def mySqrt(self, x):
        if x <= 1:
            return x
        q = 0
        pre_big = x
        pre_small = 0
        while not (q * q <= x < (q + 1) * (q + 1)):

            if q * q < x:
                print("small", q, pre_big)
                pre_small = q
                q = (int(q * 2), q + 1)[q <= 1]
                q = (q, int((pre_big + pre_small)/2) )[q >= pre_big]

            if q * q > x:
                print("big", q, pre_small)
                pre_big = q
                q = int(q * 0.5)
                q = (q, int((pre_big + pre_small)/2))[q <= pre_small]

        return q


slu = Solution()
print(slu.mySqrt(10))
