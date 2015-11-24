#!/usr/bin/python
"""
https://www.hackerrank.com/challenges/flowers
"""


class Solution:
    def __init__(self):
        self.number_of_flowers_to_buy = None
        self.number_of_friends = None
        self.prices_of_flowers = None
        self.number_bought_so_far = None
        self.total_cost = None

    def solve(self):
        self.load_task_sizes()
        self.prices_of_flowers = sorted(self.load_line())
        self.initialize_number_bought_so_far()
        self.total_cost = 0
        for _ in range(self.number_of_flowers_to_buy):
            self.buy_flower()
        self.print_solution()

    @staticmethod
    def load_line():
        return [int(number) for number in input().split(' ')]

    def load_task_sizes(self):
        self.number_of_flowers_to_buy, self.number_of_friends = self.load_line()

    def initialize_number_bought_so_far(self):
        self.number_bought_so_far = [0 for _ in range(self.number_of_friends)]

    def buy_flower(self):
        price = self.choose_most_expensive_flower()
        friend_number = self.choose_friend_that_bought_the_least()
        self.pay_and_add_flower(price, friend_number)

    def choose_most_expensive_flower(self):
        return self.prices_of_flowers.pop()

    def choose_friend_that_bought_the_least(self):
        minimum = None
        for index, number in enumerate(self.number_bought_so_far):
            if number == 0:
                return index
            if minimum is None or minimum > number:
                minimum = number
                remember = index
        return remember

    def pay_and_add_flower(self, price, friend_number):
        self.total_cost += self.compute_price(price, friend_number)
        self.number_bought_so_far[friend_number] += 1

    def compute_price(self, price, friend_number):
        return price * (self.number_bought_so_far[friend_number] + 1)

    def print_solution(self):
        print(self.total_cost)


solution = Solution()
solution.solve()
