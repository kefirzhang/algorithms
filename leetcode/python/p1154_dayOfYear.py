class Solution:
    def dayOfYear(self, date: str) -> int:
        day_num = 0
        year, month, day = map(int, date.split("-"))
        month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            month_day[2] += 1

        for i in range(month):
            day_num += month_day[i]
        # print(day_num)

        day_num += day
        # print(year, month, day)
        return day_num


slu = Solution()
print(slu.dayOfYear("2004-03-01"))
