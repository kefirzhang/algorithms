class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        pres = self.countAndSay(n - 1)  # 1

        news = ""
        val = pres[0]  # 第一个val
        num = 0
        i = 0  # 第一个指针
        j = 0  # 双指针
        length = len(pres)  # 截止点

        while j < length:
            # print(pres, i, j, num, val)
            if pres[i] == pres[j]:
                num += 1
            else:
                news = news + str(num) + val
                i = j
                num = 1
                val = pres[i]

            j += 1
        if num > 0:
            news = news + str(num) + val
        return news


slu = Solution()
print(slu.countAndSay(5))
