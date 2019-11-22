class Solution:
    def subdomainVisits(self, cpdomains):
        helper = {}
        for record in cpdomains:
            record_data = record.split(" ")
            record_data_domain = record_data[1].split('.')
            while len(record_data_domain) > 0:
                element = ".".join(record_data_domain)
                if helper.__contains__(element):
                    helper[element] = helper[element] + int(record_data[0])
                else:
                    helper[element] = int(record_data[0])
                record_data_domain.pop(0)

        helper_list = []
        for i in helper:
            helper_list.append(str(helper[i]) + " " + str(i))
        return helper_list


slu = Solution()
print(slu.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
