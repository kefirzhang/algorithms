class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        pos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        ret = ""
        import math
        while num > 0:
            addonx = pos[num % 16]
            ret = addonx + ret
            num = math.floor(num / 16)
        return ret


slu = Solution()
print(slu.toHex(-26))
