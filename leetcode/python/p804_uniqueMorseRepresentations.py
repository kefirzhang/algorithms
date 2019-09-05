class Solution:
    def uniqueMorseRepresentations(self, words):

        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---",
                 ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        map = {}
        for i in words:
            code = ''
            for j in i:
                code += morse[ord(j) - 97]
                print(code)
            if map.__contains__(code):
                continue
            else:
                map[code] = 1
        return len(map)


slu = Solution()
print(slu.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
