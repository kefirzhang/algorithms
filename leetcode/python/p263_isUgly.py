class Solution:
    def __init__(self):
        self.helper = {}

    def isUgly(self, num):

        if self.helper.__contains__(num):
            return self.helper[num]

        if num <= 0:
            return False
        if num == 1:
            return True
        base = [2, 3, 5]
        if num % 2 == 0:
            if num / 2 in base:
                self.helper[num] = True
                return True
            case2 = self.isUgly(num / 2)
        else:
            case2 = False

        if num % 3 == 0:
            if num / 3 in base:
                self.helper[num] = True
                return True
            case3 = self.isUgly(num / 3)
        else:
            case3 = False

        if num % 5 == 0:
            if num / 5 in base:
                self.helper[num] = True
                return True
            case5 = self.isUgly(num / 5)
        else:
            case5 = False

        if case2 or case3 or case5:
            self.helper[num] = True
            return True
        else:
            return False


slu = Solution()
print(slu.isUgly(2123366400))
