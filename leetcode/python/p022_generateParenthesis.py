# 这个代码写的很烂  周末总是不想解决问题  三层嵌套 脑子就不够用了
class Solution:
    def addParenthesis(self, str):  # 为字符串新增一对括号
        b_l = []
        for idx, s in enumerate(str):
            if s != '(':  # 新添加左括号
                left_str = str[:idx] + '('
                right_str = str[idx:]

                for idx_2, s_2 in enumerate(right_str):
                    if s_2 != ')':
                        b_l.append(left_str + right_str[:idx_2] + ')' + right_str[idx_2:])
                b_l.append(left_str + right_str + ')')
        b_l.append(str + '()')
        return b_l

    def addNewParenthesis(self, pre):  # 为列表新增一对括号啊
        b_l = []
        for i in pre:
            b_l += self.addParenthesis(i)
        return b_l

    def generateParenthesis(self, n):  # 新增n 对括号
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        b_l = ["()"]

        n = n - 1
        for i in range(n):  # 需要新增的n对括号
            b_l = self.addNewParenthesis(b_l)
        r_l = []
        dict = {}
        for r in b_l:
            if r not in dict:
                r_l.append(r)
                dict[r] = r

        return r_l


slu = Solution()
print(slu.generateParenthesis(3))
