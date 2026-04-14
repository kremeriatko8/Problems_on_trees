'''
Definition for Employee.
'''

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        employees_dict = {}
        for emp in employees:
            employees_dict[emp.id] = emp

        def dfs(emp_id):
            employee = employees_dict[emp_id]

            answer = employee.importance
            for sub_id in employee.subordinates:
                answer += dfs(sub_id)
            return answer

        return dfs(id)
