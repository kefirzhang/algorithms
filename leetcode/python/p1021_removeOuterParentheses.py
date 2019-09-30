class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        back = ''
        helper = []
        helper_2 = []
        for i in S:
            if len(helper) == 0:
                helper.append(i)
            elif len(helper) == 1:
                if i == ')':
                    helper.pop()
                    back = back + "".join(helper_2)
                    helper_2 = []
                else:
                    helper.append(i)
                    helper_2.append(i)
            else:
                helper_2.append(i)
                if helper[-1] == '(' and i == ')':
                    helper.pop()
                else:
                    helper.append(i)
        return back


slu = Solution()
print(slu.removeOuterParentheses("(((((())))))"))

'''
"(()())(())(()(()))"
"(((((())))))"
'''
