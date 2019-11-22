class Solution:
    def isValid(self, s):
        list = []
        cfg = {'(': ')', '[': ']', '{': '}',')': '(', ']': '[', '}': '{'}
        for i in s:
            if len(list) == 0:
                list.append(i)
            else:
                if i == cfg[list[-1]]:
                    list.pop()
                else:
                    list.append(i)
        if len(list) == 0:
            return True
        else:
            return False


slu = Solution()
print(slu.isValid("(()[]{})"))
