class Solution:
    def hasGroupsSizeX(self, deck):
        helper = {}
        for card in deck:
            if helper.__contains__(card):
                helper[card] += 1
            else:
                helper[card] = 1
        i = 2
        while i <= helper[card]:
            status = True
            for j in helper:
                if helper[j] % i != 0:
                    status = False
                    break
            if status is True:
                return True
            i += 1

        return False


slu = Solution()
print(slu.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1, 1]))
