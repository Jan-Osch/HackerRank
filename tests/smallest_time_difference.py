"""
https://www.hackerrank.com/tests/4tsdod0a95k/questions/g7o3adndkaa
"""


class Solution:
    def __init__(self, string_times):
        self.times = []
        self.smallest_difference = None
        self.string_times = string_times

    def solve(self):
        self.load_times(self.string_times)
        self.compute_differences()
        self.print_minimum()

    def load_times(self, times_to_parse):
        for time in times_to_parse:
            self.times.append(self.to_minutes(time.split(':')))

    @staticmethod
    def to_minutes(time):
        return 60 * int(time[0]) + int(time[1])

    def compute_differences(self):
        for first_index, first_time in enumerate(self.times):
            for second_index, second_time in enumerate(self.times):
                if first_index != second_index:
                    self.compare_times(first_time, second_time)

    def compare_times(self, first_time, second_time):
        first_to_second_difference = self.compute_forward_difference(first_time, second_time)
        self.compare_to_minimum(first_to_second_difference)
        second_to_firs_difference = self.compute_forward_difference(second_time, first_time)
        self.compare_to_minimum(second_to_firs_difference)

    @staticmethod
    def compute_forward_difference(first_time, second_time):
        if second_time - first_time < 0:
            return second_time + 24 * 60 - first_time
        return second_time - first_time

    def compare_to_minimum(self, difference):
        if self.smallest_difference is None or self.smallest_difference > difference:
            self.smallest_difference = difference

    def print_minimum(self):
        print(self.smallest_difference)


def getMinTimeDifference(times):
    solution = Solution(times)
    solution.solve()
