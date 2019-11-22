class Solution:
    def isAlienSorted(self, words, order) -> bool:
        def compareStr(word1, word2):
            len1 = len(word1)
            len2 = len(word2)
            i = 0
            while i < len2:
                if i > len1 - 1:
                    return False
                if helper_order.index(word2[i]) == helper_order.index(word1[i]):
                    i += 1
                    continue
                elif helper_order.index(word2[i]) > helper_order.index(word1[i]):
                    return True
                else:
                    return False
            if i < len1 - 1:
                return False
            return True

        helper_order = list(order)
        pre_word = words[0]
        words.pop(0)
        for word in words:
            if compareStr(pre_word, word) is False:
                return False
            pre_word = word
        return True


slu = Solution()
print(slu.isAlienSorted(
    ["zirqhpfscx", "zrmvtxgelh", "vokopzrtc", "nugfyso", "rzdmvyf", "vhvqzkfqis", "dvbkppw", "ttfwryy", "dodpbbkp",
     "akycwwcdog"], "khjzlicrmunogwbpqdetasyfvx"))
