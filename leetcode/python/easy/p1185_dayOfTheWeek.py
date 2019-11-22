class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        helper = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if month == 1 or month == 2:
            month += 12
            year -= 1
        w = (day + 2 * month + int((3 * (month + 1)) / 5) + year + int(year / 4) - int(year / 100) + int(
            year / 400) + 1) % 7
        return helper[w - 1]


slu = Solution()
print(slu.dayOfTheWeek(16, 10, 2019))
'''

    if (month == 1 || month == 2)
    {
        month += 12;
        --year;
    }
 
    int week = -1;
    week = (day + 2 * month + 3 * (month + 1) / 5 + year + year / 4 - year / 100 + year / 400) % 7 + 1;
    return week; 
————————————————
版权声明：本文为CSDN博主「无名小刺猬」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ylwshzh/article/details/45875125
'''
