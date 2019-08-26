class Solution:
    def romanToInt(self, s):
        maps = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                "IV": 4,
                "IX": 9,
                "XL": 40,
                "XC": 90,
                "CD": 400,
                "CM": 900,
                }

        sum_num = 0
        continue_status = False
        for i, n in enumerate(s):
            if continue_status:
                continue_status = False
                continue

            if (maps.get(s[i:i + 2], "") != ""):
                continue_status = True
                sum_num = sum_num + maps.get(s[i:i + 2], "")
            else:
                sum_num += maps.get(n)
        return sum_num



