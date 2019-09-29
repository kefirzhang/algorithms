class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        len1 = len(start)
        len2 = len(end)
        if len1 != len2:
            return False
        i = 0
        j = 0
        while i < len1 and j < len2:
            while start[i] == 'X' and i < len1 - 1:
                i += 1

            while end[j] == 'X' and j < len2 - 1:
                j += 1

            if start[i] != end[j]:
                return False

            elif start[i] == 'R':
                if i > j:
                    return False
            elif start[i] == 'L':
                if i < j:
                    return False
            i += 1
            j += 1

        return True


slu = Solution()
print(slu.canTransform("XXXXXRXXXX", "RXXXXXXXXX"))
"XXXXXLXXXX"
"LXXXXXXXXX"

"XXRXXLXXXX"
"XXXXRXXLXX"

"XXXXXLXXXX"
"LXXXXXXXXX"

'''
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，
当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-adjacent-in-lr-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
