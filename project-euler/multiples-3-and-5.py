#!/usr/bin/python
"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler001
"""


class Solution:
    def __init__(self):
        self.current_sum = None
        self.number_of_test_cases = None
        self.current_limit = None
        self.found_sums = {1: 0}
        self.tested_cases = [1]
        self.cases_to_test = []

    def solve(self):
        self.load_number_of_test_cases()
        self.load_cases_to_test(self.number_of_test_cases)
        for case in self.cases_to_test:
            self.solve_case(case)
            self.print_solution()

    def load_cases_to_test(self, number):
        for _ in range(number):
            self.cases_to_test.append(int(input()))

    def load_number_of_test_cases(self):
        self.number_of_test_cases = int(input())

    def solve_case(self, case):
        self.current_limit = case
        if self.current_limit in self.tested_cases:
            self.current_sum = self.found_sums[self.current_limit]
        else:
            self.solve_new_case()

    def print_solution(self):
        print(self.current_sum)

    def solve_new_case(self):
        self.current_sum = 0
        self.explore_bounds(1, self.current_limit)

    def explore_bounds(self, lower_limit, upper_limit):
        first_multiple_of_both = self.iterate_until_multiple_of_both(lower_limit, upper_limit)
        self.step_over_multiples(first_multiple_of_both, upper_limit)

    def iterate_until_multiple_of_both(self, lower_limit, upper_limit):
        for candidate in range(lower_limit, upper_limit):
            if self.is_multiple_of_both(candidate):
                return candidate
            if self.is_multiple_at_least_one(candidate):
                self.current_sum += candidate
        return upper_limit

    def step_over_multiples(self, left_limit, right_limit):
        if self.limits_are_valid(left_limit, right_limit):
            self.step_over_multiples_of_3(left_limit, right_limit)
            self.step_over_multiples_of_5(left_limit, right_limit)

    def step_over_multiples_of_3(self, left_limit, right_limit):
        if self.limits_are_valid(left_limit, right_limit):
            self.current_sum += self.compute_sum_of_range(left_limit, right_limit, 3)

    def step_over_multiples_of_5(self, left_limit, right_limit):
        if self.limits_are_valid(left_limit, right_limit):
            self.current_sum += self.compute_sum_of_range(left_limit + 5, right_limit, 15)
            self.current_sum += self.compute_sum_of_range(left_limit + 10, right_limit, 15)

    @staticmethod
    def is_multiple_of_both(candidate):
        return (candidate // 3) * 3 == candidate and (candidate // 5) * 5 == candidate

    @staticmethod
    def is_multiple_at_least_one(candidate):
        return (candidate // 3) * 3 == candidate or (candidate // 5) * 5 == candidate

    @staticmethod
    def limits_are_valid(left_limit, right_limit):
        return left_limit < right_limit

    @staticmethod
    def compute_sum_of_range(left_limit, right_limit, step):
        number = (right_limit - left_limit - 1) // step
        last_element = left_limit + step * number
        return int(((left_limit + last_element) * (number + 1) // 2))


solution = Solution()
solution.solve()
