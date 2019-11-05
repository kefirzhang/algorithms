class Solution:
    def letterCasePermutation(self, S):
        def all(characters):
            if len(characters) == 1:
                if ord('a') <= ord(characters[0]) <= ord('z') or ord('A') <= ord(characters[0]) <= ord('Z'):
                    return [characters[0].upper(), characters[0].lower()]
                else:
                    return [characters[0]]

            ret = []
            others = all(characters[1:])
            for i in others:
                if ord('a') <= ord(characters[0]) <= ord('z') or ord('A') <= ord(characters[0]) <= ord('Z'):
                    ret.append(characters[0].upper() + i)
                    ret.append(characters[0].lower() + i)
                else:
                    ret.append(characters[0] + i)

            return ret

        S = list(S)

        return all(S)


slu = Solution()
print(slu.letterCasePermutation("a1b2"))
