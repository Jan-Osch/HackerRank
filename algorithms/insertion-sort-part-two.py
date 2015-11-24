#!/usr/bin/python
"""
https://www.hackerrank.com/challenges/insertionsort2
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
        for starting_index in range(1, self.size):
            index, last_element = self.sort_from_index(starting_index)
            self.array[index + 1] = last_element
            self.print_current_state()

    def load_data(self):
        self.size = int(input())
        self.array = self.load_array()

    def sort_from_index(self, index):
        last_element = self.array[index]
        index -= 1
        while index >= 0 and self.shift_cell_at_index(index, last_element):
            index -= 1
        return index, last_element

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
