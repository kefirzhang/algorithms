class Solution:
    def numUniqueEmails(self, emails) -> int:
        def init_email(address):
            address = address.split("@")
            address[0] = address[0].replace(".", "")
            address[0] = (address[0].split("+"))[0]
            address = "@".join(address)
            # print(address)
            return address

        helper = set()
        for email in emails:
            helper.add(init_email(email))
        return len(helper)


slu = Solution()
print(slu.numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
