class Solution:
    key_map = {
        "1": [""],
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits):
        s_l = []  # 存储的list
        for i in digits:  # 遍历字符
            p_l = []
            for j in self.key_map.get(i):  # 获取对应的map 根上一层是一层的
                if len(s_l) == 0:
                    p_l.append(j)
                    continue
                for k in s_l:
                    p_l.append(k + j)

            s_l = p_l
        return s_l


slu = Solution()
print(slu.letterCombinations("23"))
