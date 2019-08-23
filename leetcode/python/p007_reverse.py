# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 123 321
class Solution:
    def reverse(self, x):
        reverse_x = 0
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        pre = True
        base = 10
        if x < 0:
            pre = False
            base = -10

        x = abs(x)
        while x != 0:
            p = x % 10
            x = int(x / 10)

            if reverse_x > INT_MAX / 10 or (reverse_x == INT_MAX / 10 and p > 7):
                return 0

            reverse_x = reverse_x * 10 + p

            # python 除法不一样
            # if (rev > INT_MAX / 10 | | (rev == INT_MAX / 10 & & pop > 7)) return 0;
            # if (rev < INT_MIN / 10 | | (rev == INT_MIN / 10 & & pop < -8)) return 0;

        if pre:
            return reverse_x
        else:
            if -reverse_x < INT_MIN:
                return 0
            return -reverse_x


solution = Solution()
print(solution.reverse(-2147483649))
