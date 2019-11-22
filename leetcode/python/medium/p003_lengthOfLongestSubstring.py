# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
class Solution:
    def lengthOfLongestSubstring(self, str):
        length = len(str)
        start = 1
        maxlen = 0
        saveList = []
        while start <= length:
            if len(saveList) > 0 and saveList.count(str[start - 1]) > 0:
                maxlen = max(maxlen, len(saveList))
                newListIndex = saveList.index(str[start - 1]) + 1
                saveList.append(str[start - 1])
                saveList = saveList[newListIndex:]
            else:
                saveList.append(str[start - 1])

            start += 1

        maxlen = max(maxlen, len(saveList))
        return maxlen


solution = Solution()

print(solution.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz"))
