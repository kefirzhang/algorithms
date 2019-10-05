class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        helper = {}
        list_data = A.split(" ") + B.split(" ")
        for i in list_data:
            if helper.__contains__(i):
                helper[i] = helper[i] + 1
            else:
                helper[i] = 1
        helper_list = []
        for i in helper:
            if helper[i] == 1:
                helper_list.append(i)
        return helper_list


slu = Solution()
print(slu.uncommonFromSentences("this apple is sweet", "this apple is sour"))
