# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        helper = {}
        for employee in employees:
            helper[employee.id] = employee

        importance = helper[id].importance
        for idx in helper[id].subordinates:
            importance += self.getImportance(employees, idx)
        return importance


e1 = Employee(1, 15, [2])
e2 = Employee(2, 10, [3])
e3 = Employee(3, 5, [])
slu = Solution()
print(slu.getImportance([e1, e2, e3], 1))

'''
[[1,5,[2,3]],[2,3,[4]],[3,4,[]],[4,1,[]]]
1
'''
