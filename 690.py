"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        #
        # transform emplyees to dict (from list)
        #
        employees = {emp.id: emp for emp in employees}
        #
        # perform BFS
        #
        idQueue = [id]
        total = 0
        while len(idQueue) > 0:
            # (1) dequeue (2) add its importance (3) enqueue its subordinate IDs
            empID = idQueue.pop(0)
            total += employees[empID].importance
            idQueue += employees[empID].subordinates
        return total
        
        