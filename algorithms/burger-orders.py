#!/usr/bin/python
"""
https://www.hackerrank.com/challenges/jim-and-the-orders
"""


class Solution:
    def __init__(self):
        self.number_of_fans = None
        self.time_to_fan_map = {}

    def solve(self):
        self.load_size()
        for fan_number in range(1, self.number_of_fans + 1):
            time_to_order, duration = self.load_line()
            self.add_order_to_map(fan_number, time_to_order, duration)
        self.print_array(self.extract_order_from_map())

    def load_size(self):
        self.number_of_fans = int(input())

    @staticmethod
    def load_line():
        return [int(number) for number in input().split(' ')]

    def add_order_to_map(self, fan_number, time_to_order, duration):
        time_to_finish = time_to_order + duration
        if time_to_finish in self.time_to_fan_map.keys():
            self.time_to_fan_map[time_to_finish].append(fan_number)
        else:
            self.time_to_fan_map[time_to_finish] = [fan_number]

    def extract_order_from_map(self):
        result = []
        time = 1
        while len(result) < self.number_of_fans:
            if time in self.time_to_fan_map.keys():
                result.extend(self.time_to_fan_map[time])
            time += 1
        return result

    @staticmethod
    def print_array(array):
        print(' '.join([str(number) for number in array]))


solution = Solution()
solution.solve()
