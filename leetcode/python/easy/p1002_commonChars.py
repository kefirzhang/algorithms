class Solution:
    def commonChars(self, A):
        helper = list(A[0])
        A.pop(0)
        for record in A:
            adjust_helper = []
            record_list = list(record)
            for i in helper:
                if i in record_list:
                    adjust_helper.append(i)
                    record_list.remove(i)
            helper = adjust_helper
        return helper


slu = Solution()
print(slu.commonChars(["cool", "lock", "cook"]))
