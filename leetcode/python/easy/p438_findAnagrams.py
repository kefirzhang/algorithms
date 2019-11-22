# 可以用滑动窗口 先找到第一个 然后一直滑动就可以了
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t) or len(s) == 0 or len(t) == 0:
            return False
        pre_map = {}
        for i in s:
            if pre_map.__contains__(i):
                pre_map[i] += 1
            else:
                pre_map[i] = 1
        for j in t:
            if not pre_map.__contains__(j):
                return False
            pre_map[j] -= 1
            if pre_map[j] == 0:
                del pre_map[j]
        if len(pre_map) == 0:
            return True
        else:
            return False

    def findAnagrams(self, s, p):
        s_len = len(s)
        p_len = len(p)
        idx_l = []
        idx = 0
        pre = False  # 前一个是不是匹配
        while idx < s_len:
            if idx + p_len > s_len:
                break
            if pre and idx > 0 and s[idx - 1] == s[idx + p_len - 1]:
                idx_l.append(idx)
                pre = True
            elif pre is False and idx > 0 and s[idx - 1] == s[idx + p_len - 1]:
                pre = False
            elif self.isAnagram(s[idx:idx + p_len], p):
                idx_l.append(idx)
                pre = True
            else:
                pre = False
            idx += 1

        return idx_l


slu = Solution()
print(slu.findAnagrams("cabcdeabab", "ab"))
