class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or A == "":
            return False
        same, index_1, index_2 = True, -1, -1
        for i, n in enumerate(A):
            if A[i] != B[i]:
                same = False
                if index_1 == -1:
                    index_1 = i
                elif index_2 == -1:
                    index_2 = i
                else:
                    return False
        if same:
            if len(set(list(A))) < len(A):
                return True
            else:
                return False
        elif A[index_1] == B[index_2] and A[index_2] == B[index_1]:
            return True

        return False


slu = Solution()
print(slu.buddyStrings("ab", "ab"))
