class Solution:
    def fizzBuzz(self, n: int):
        ret = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ret.append("FizzBuzz")
            elif i % 5 == 0:
                ret.append("Buzz")
            elif i % 3 == 0:
                ret.append("Fizz")
            else:
                ret.append(str(i))
        return ret


slu = Solution()
print(slu.fizzBuzz(20))
