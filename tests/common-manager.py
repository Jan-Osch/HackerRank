"""
https://www.hackerrank.com/tests/3elt34nh9kn/questions/64eq80i7hk7
"""


class Solution:
    def __init__(self, company_size):
        self.company_size = company_size
        self.first_employee = None
        self.second_employee = None
        self.superior_map = {}
        self.visited_employees = []
        self.common_manager = None

    def solve(self):
        self.load_selected_employees()
        for _ in range(self.company_size - 1):
            self.load_relationship()
        self.find_common_manager()
        print(self.common_manager)

    def load_relationship(self):
        superior, subordinate = input().split(' ')
        self.superior_map[subordinate] = superior

    def load_selected_employees(self):
        self.first_employee = input()
        self.second_employee = input()

    def find_common_manager(self):
        current_employee = self.first_employee
        next_employee = self.second_employee
        while self.common_manager is None:
            self.visit_employee(current_employee)
            current_employee = self.select_next_from_hierarchy(current_employee)
            current_employee, next_employee = next_employee, current_employee

    def visit_employee(self, employee_name):
        if employee_name in self.visited_employees:
            self.common_manager = employee_name
        self.visited_employees.append(employee_name)

    def select_next_from_hierarchy(self, first):
        if first in self.superior_map.keys():
            return self.superior_map[first]
        return None


def OutputCommonManager(count):
    solution = Solution(count)
    solution.solve()
