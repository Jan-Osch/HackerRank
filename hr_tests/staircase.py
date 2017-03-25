#!/usr/bin/python
"""
https://www.hackerrank.com/tests/sample/questions/c18sp5qibki
"""


class Solution:
    def __init__(self):
        self.number_of_stairs = None

    def solve(self):
        self.load_number_of_stairs()
        for number_of_hashes in range(1, self.number_of_stairs + 1):
            self.print_stair_level(number_of_hashes)

    def load_number_of_stairs(self):
        self.number_of_stairs = int(input())

    def print_stair_level(self, number_of_hashes):
        empty_spaces = self.generate_spaces(self.number_of_stairs - number_of_hashes)
        print (empty_spaces + self.generate_hashes(number_of_hashes))

    @staticmethod
    def generate_spaces(number):
        return ''.join([' ' for _ in range(number)])

    @staticmethod
    def generate_hashes(number_of_hashes):
        return ''.join(['#' for _ in range(number_of_hashes)])


solution = Solution()
solution.solve()
