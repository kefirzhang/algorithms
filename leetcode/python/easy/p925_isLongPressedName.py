class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        len_name, len_typed = len(name), len(typed)
        while i < len_name or j < len_typed:
            i_times = 1
            j_times = 1
            while i < len_name - 1 and name[i] == name[i + 1]:
                i += 1
                i_times += 1
            while j < len_typed - 1 and typed[j] == typed[j + 1]:
                j += 1
                j_times += 1

            # print(i, j, name[i], typed[j])
            if name[i] != typed[j] or i_times > j_times:
                return False
            if (i == len_name - 1 and j != len_typed - 1) or (i != len_name - 1 and j == len_typed - 1):
                return False
            i += 1
            j += 1
        return True


slu = Solution()
print(slu.isLongPressedName("alex", "aaleex"))
'''
"pyplrz"
"ppyypllr"

"alex"
"aaleex"
'''
