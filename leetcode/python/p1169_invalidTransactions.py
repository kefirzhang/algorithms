class Solution:
    def invalidTransactions(self, transactions):
        helper = []
        helper_back = []
        for transaction in transactions:
            tmp_transaction = transaction.split(",")
            helper.append(tmp_transaction)

        for record in helper:
            if int(record[2]) > 1000:
                helper_back.append(",".join(record))
            else:
                for record2 in helper:
                    if record[0] == record2[0] and record[3] != record2[3] and abs(int(record[1])-int(record2[1])) <= 60:
                        helper_back.append(",".join(record))
                        break
        return helper_back


slu = Solution()
print(slu.invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
