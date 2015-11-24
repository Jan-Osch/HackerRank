#!/usr/bin/python
"""
https://www.hackerrank.com/challenges/2d-array
"""


class Solution:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.biggest_sum = None
        self.array = None

    @staticmethod
    def load_row():
        return [int(number) for number in input().split(' ')]

    def load_2d_array(self, rows, columns):
        return [self.load_row() for _ in range(rows)]

    def compute_hourglass_for_coordinates(self, x, y):
        hourglass_sum = self.array[y - 1][x - 1]
        hourglass_sum += self.array[y - 1][x]
        hourglass_sum += self.array[y - 1][x + 1]
        hourglass_sum += self.array[y][x]
        hourglass_sum += self.array[y + 1][x - 1]
        hourglass_sum += self.array[y + 1][x]
        hourglass_sum += self.array[y + 1][x + 1]
        return hourglass_sum

    def coordinates_are_valid_for_hourglass(self, x, y):
        if 0 < x < self.columns - 1:
            if 0 < y < self.rows - 1:
                return True
        return False

    def compare_sum_and_save_it(self, candidate_sum):
        if self.biggest_sum is None or self.biggest_sum < candidate_sum:
            self.biggest_sum = candidate_sum

    def find_biggest_sum(self):
        for y in range(self.rows):
            for x in range(self.columns):
                if self.coordinates_are_valid_for_hourglass(x, y):
                    self.compare_sum_and_save_it(self.compute_hourglass_for_coordinates(x, y))

    def print_solution(self):
        print (self.biggest_sum)

    def solve(self):
        self.array = self.load_2d_array(self.rows, self.columns)
        self.find_biggest_sum()
        self.print_solution()

    def print_array(self):
        for row in self.array:
            self.print_row(row)

    @staticmethod
    def print_row(row):
        print (row)


solution = Solution(6, 6)
solution.solve()
