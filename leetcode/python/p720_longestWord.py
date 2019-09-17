class Solution:
    def longestWord(self, words):
        max_str = ''
        for i in words:
            if len(i) < len(max_str):
                continue
            if len(i) == len(max_str) and i > max_str:
                continue

            tmp_str = ''
            is_val_str = True
            for j in i:
                tmp_str += j
                if tmp_str not in words:
                    is_val_str = False
            if is_val_str:
                if len(max_str) < len(i):
                    max_str = i
                elif len(max_str) == len(i) and i < max_str:
                    max_str = i
        return max_str


slu = Solution()
print(slu.longestWord(["rac", "rs", "ra", "on", "r", "otif", "o", "onpdu", "rsf", "rs", "ot", "oti", "racy", "onpd"]))
