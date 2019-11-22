class Solution:
    def numSmallerByFrequency(self, queries, words):
        ret = []
        words_count = [word.count(min(word)) for word in words]
        for query in queries:
            query_count = query.count(min(query))
            ret.append(len([count for count in words_count if count > query_count]))
        return ret


slu = Solution()
print(slu.numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"]))

'''
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        ret, queries_count, words_count = [], [], []
        words_count = [word.count(min(word)) for word in words]
        for query in queries:
            c = query.count(min(query))
            # 在 words_count 里数一下有多少是比 c 大的
            ret.append(len([x for x in words_count if c < x]))
        return ret

作者：philhsu
链接：https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character/solution/python-by-philhsu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
