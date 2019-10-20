class Solution:
    def reorderLogFiles(self, logs):
        def compare(a, b):
            a = a.split(" ")
            b = b.split(" ")

            if " ".join(a[1:]) == " ".join(b[1:]):
                if a[0] > b[0]:
                    return 1
                elif a[0] == b[0]:
                    return 0
                else:
                    return -1
            else:
                if " ".join(a[1:]) > " ".join(b[1:]):
                    return 1
                else:
                    return -1
        num_helper = []
        str_helper = []
        for log in logs:
            if log.split(" ")[1].isdigit():
                num_helper.append(log)
            else:
                str_helper.append(log)
        # print(num_helper, str_helper)

        for i in range(0, len(str_helper)):
            for j in range(1 + i, len(str_helper)):
                if compare(str_helper[i], str_helper[j]) == 1:
                    str_helper[i], str_helper[j] = str_helper[j], str_helper[i]

        return str_helper + num_helper


slu = Solution()
print(slu.reorderLogFiles(["j mo", "5 m w", "g 07", "o 2 0", "t q h"]))
