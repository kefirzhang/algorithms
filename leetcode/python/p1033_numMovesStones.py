class Solution:
    def numMovesStones(self, a: int, b: int, c: int):
        pos = [a, b, c]
        pos.sort()
        x = pos[0]
        y = pos[1]
        z = pos[2]

        if x + 1 == y and y + 1 == z:
            return [0, 0]
        if x < y < z:
            max = z - x - 2 if z - x - 2 > 0 else 0

            if x + 1 == y or y + 1 == z or x + 2 == y or y + 2 == z:
                min = 1
            else:
                min = 2
            return [min, max]
        else:
            return [0, 0]


slu = Solution()
print(slu.numMovesStones(3, 5, 1))

'''
[1,2]3, 5, 1
三枚石子放置在数轴上，位置分别为 a，b，c。

每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/moving-stones-until-consecutive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
