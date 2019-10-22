class Solution:
    def lemonadeChange(self, bills) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            if i == 10:
                ten += 1
                five -= 1
            elif i == 20:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0 or ten < 0:
                return False
        return True

slu = Solution()
print(slu.lemonadeChange([5, 5, 5, 10, 20]))
