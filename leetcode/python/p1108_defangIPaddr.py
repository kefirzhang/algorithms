class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join((address.split(".")))

slu = Solution()
print(slu.defangIPaddr("1.1.1.1"))