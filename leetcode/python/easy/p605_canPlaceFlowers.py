class Solution:
    def canPlaceFlowers(self, flowerbed, num):
        end = len(flowerbed) - 1
        pre = True  # 前面是否有空位
        total = 0
        for i, n in enumerate(flowerbed):
            if n == 1:
                pre = False
                continue
            elif n == 0:
                if pre is True:
                    if i == end or flowerbed[i + 1] == 0:
                        total += 1
                        pre = False
                    else:
                        pre = True
                else:
                    pre = True
        print(total, num)
        return total >= num


slu = Solution()
print(slu.canPlaceFlowers([1, 0, 0, 0, 1], 2))
