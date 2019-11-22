class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_helper = []
        guess_helper = []
        secret = list(secret)
        guess = list(guess)
        i = 0
        while i < len(secret) and i < len(guess):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_helper.append(secret[i])
                guess_helper.append(guess[i])
            i += 1
        secret_helper += secret[i:]
        guess_helper += guess[i:]

        for i in secret_helper:
            if i in guess_helper:
                guess_helper.remove(i)
                cows += 1

        return str(bulls) + "A" + str(cows) + "B"


slu = Solution()
print(slu.getHint("1807", "7810"))
