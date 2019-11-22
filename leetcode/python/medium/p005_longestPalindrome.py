class Solution:
    def longestPalindrome(self, string):
        length = len(string) - 1
        index = 0
        max_step = 0
        max_str = ""
        max_type = 1
        while index <= length:

            o_step = 0
            e_step = 0

            while (index - o_step >= 0) and (index + o_step <= length) and (  # 奇数
                    string[index - o_step] == string[index + o_step]):
                o_step += 1

            while (index - e_step >= 0) and (index + e_step + 1 <= length) and (  # 偶数
                    string[index - e_step] == string[index + e_step + 1]):
                e_step += 1

            if e_step >= o_step and (e_step > max_step or (max_type == 1 and e_step == max_step)):  # 偶数
                max_step = e_step
                max_type = 0
                max_str = string[index - e_step + 1:index + e_step + 1]
            elif o_step > e_step and o_step > max_step:  # 奇数
                max_step = o_step
                max_type = 1
                max_str = string[index - o_step + 1:index + o_step]

            index += 1

        return max_str


solution = Solution()
print(solution.longestPalindrome("ababbbb"))
