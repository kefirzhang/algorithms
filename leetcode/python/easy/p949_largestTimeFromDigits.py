class Solution:
    def largestTimeFromDigits(self, A) -> str:
        helper = []
        for i in range(4):
            hour_1 = A[i]
            if hour_1 > 2:
                continue
            A_1 = A[0:i] + A[i + 1:]
            for j in range(3):
                hour_2 = A_1[j]
                if hour_1 == 2 and hour_2 > 3:
                    continue
                A_2 = A_1[0:j] + A_1[j + 1:]
                for k in range(2):

                    if k == 0:
                        minute_1 = A_2[0]
                        minute_2 = A_2[1]
                    else:
                        minute_1 = A_2[1]
                        minute_2 = A_2[0]
                    if minute_1 > 5:
                        continue
                    # print(hour_1, hour_2, minute_1, minute_2)
                    helper.append(hour_1 * 1000 + hour_2 * 100 + minute_1 * 10 + minute_2)
        # print(helper)
        if len(helper) == 0:
            return ""
        ret = str(max(helper))
        if len(ret) == 4:
            return ret[0:2] + ":" + ret[-2:]
        elif len(ret) == 3:
            return "0" + ret[0] + ":" + ret[1:]
        elif len(ret) == 2:
            return "00:" + ret
        elif len(ret) == 1:
            return "00:0" + ret[-1]


slu = Solution()
print(slu.largestTimeFromDigits([0, 4, 0, 0]))
