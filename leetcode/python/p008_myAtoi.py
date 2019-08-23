class Solution:
    def myAtoi(self, string):
        num = 0
        length = len(string)
        idx = 0
        positive = None  # 是否是正数 默认0 正数
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        while idx < length:

            cur_s = string[idx]

            if cur_s >= '0' and cur_s <= '9':
                cur_s = int(cur_s)
                if positive is None:
                    positive = True

                if positive:
                    if num > INT_MAX / 10 or (num == int(INT_MAX / 10) and cur_s > 7):
                        return INT_MAX
                    num = num * 10 + int(cur_s)
                else:
                    if num < INT_MIN / 10 or (num == int(INT_MIN / 10) and -cur_s < -8):
                        return INT_MIN
                    num = abs(num) * -10 - int(cur_s)
            elif cur_s == '-' and num == 0 and positive is None:
                positive = False
            elif cur_s == '+' and num == 0 and positive is None:
                positive = True
            elif num != 0 or positive is not None or cur_s != " ":
                return num
            idx += 1
        return num


solution = Solution()
print(solution.myAtoi('-2147483649'))
