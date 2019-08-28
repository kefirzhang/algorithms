class Solution:
    def compress(self, chars):
        length = len(chars)
        i = j = k = num = 0
        while j < length:
            if chars[i] == chars[j]:
                num += 1
            else:
                chars[k] = chars[i]
                if num > 1:
                    for n in str(num):
                        chars[k + 1] = n
                        k += 1
                k += 1
                i = j
                num = 1
            j += 1

        chars[k] = chars[i]
        if num > 1:
            for n in str(num):
                chars[k + 1] = n
                k += 1
        k += 1
        return k


slu = Solution()
print(slu.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
