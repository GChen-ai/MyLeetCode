"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        if employees==None or len(employees)==0:
            return 0
        dic={}
        for e in employees:
            dic[e.id]=e
        def dfs(cur):
            sum_i=dic[cur].importance
            for i in dic[cur].subordinates:
                sum_i+=dfs(i)
            return sum_i
        result=dfs(id)
        return result
