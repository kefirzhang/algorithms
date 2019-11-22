class Solution:
    def selfDividingNumbers(self, left: int, right: int) :
        def isSelfDivNum(num):
            helper = list(str(num))
            for i in helper:
                i = int(i)
                if i == 0:
                    return False
                if num % i != 0:
                    return False
            return True

        ret = []
        for i in range(left,right+1):
            if isSelfDivNum(i):
                ret.append(i)
        return ret


slu = Solution()
print(slu.selfDividingNumbers(1, 22))
