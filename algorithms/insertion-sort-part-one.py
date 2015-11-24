#!/usr/bin/python
"""
https://www.hackerrank.com/challenges/insertionsort1
"""


class Solution:
    def __init__(self):
        self.array = None
        self.size = None

    @staticmethod
    def load_array():
        return [int(number) for number in input().split(' ')]

    def solve(self):
        self.load_data()
        last_element = self.array[-1]
        index = self.shift_cells(last_element)
        self.array[index + 1] = last_element
        self.print_current_state()

    def load_data(self):
        self.size = int(input())
        self.array = self.load_array()

    def shift_cells(self, last_element):
        index = self.size - 2
        while index >= 0 and self.shift_cell_at_index(index, last_element):
            self.print_current_state()
            index -= 1
        return index

    def print_current_state(self):
        result = [str(number) for number in self.array]
        print (' '.join(result))

    def shift_cell_at_index(self, index, original_number):
        if self.array[index] > original_number:
            self.array[index + 1] = self.array[index]
            return True
        return False


solution = Solution()
solution.solve()
