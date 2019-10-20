class Solution:
    def numSpecialEquivGroups(self, A) -> int:
        helper = set()
        for word in A:
            word = "".join(sorted(word[::2]) + sorted(word[1::2]))
            helper.add(word)
        return len(helper)


slu = Solution()
print(slu.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))

'''
def numSpecialEquivGroups(self, A: List[str]) -> int:
    res = set()
    for sub in A:
        sub = ''.join(sorted(sub[::2]) + sorted(sub[1::2]))
        res.add(sub)
    return len(res)

作者：cong-6
链接：https://leetcode-cn.com/problems/groups-of-special-equivalent-strings/solution/te-shu-deng-jie-zi-fu-chuan-zu-python3-by-cong-6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
