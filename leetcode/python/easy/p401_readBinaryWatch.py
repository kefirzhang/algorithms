class Solution:
    def readBinaryWatch(self, num: int):
        def getCombine(arr, k):
            ret = []
            if k == 0:
                return ret
            length = len(arr)
            if k >= length:
                return [arr]
            for i, n in enumerate(arr):
                exts = getCombine(arr[i + 1:], k - 1)
                if len(exts) == 0:
                    ret.append([n])
                else:
                    for ext in exts:
                        if len(ext) == k - 1:
                            ret.append([n] + ext[::])
            return ret

        ret = []
        hour_bit = [8, 4, 2, 1]
        minute_bit = [32, 16, 8, 4, 2, 1]

        for i in range(num + 1):
            j = num - i
            if i > 3 or j > 5:
                continue

            hours = getCombine(hour_bit, i)
            minutes = getCombine(minute_bit, j)
            # print(hours, i)
            # print(minutes, j)
            if len(hours) == 0:
                hours = [[0]]
            if len(minutes) == 0:
                minutes = [[0]]
            for hour in hours:
                hour = sum(hour)
                if hour > 11:
                    continue
                hour = str(hour)
                for minute in minutes:
                    minute = sum(minute)
                    if minute > 59:
                        continue
                    minute = str(minute)
                    if len(minute) == 1:
                        minute = "0" + minute
                    ret.append(hour + ":" + minute)

        return ret


slu = Solution()
print(slu.readBinaryWatch(6))
