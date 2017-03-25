"""
https://www.hackerrank.com/tests/4tsdod0a95k/questions/8o7oioj07g7
"""


class Solution:
    def __init__(self, transactions, amount_fraud_limit, time_fraud_limit):
        self.detected_frauds = {}
        self.transactions = transactions
        self.amount_fraud_limit = amount_fraud_limit
        self.time_fraud_limit = time_fraud_limit
        self.previous_transaction_city = {}
        self.previous_transaction_time = {}

    def solve(self):
        for transaction in self.transactions:
            self.analyse_transaction(transaction)
        return self.sort_by_detection_time(self.detected_frauds)

    @staticmethod
    def parse_transaction(transaction):
        parsed = transaction.split('|')
        return parsed[0], int(parsed[1]), parsed[2], int(parsed[3])

    def analyse_transaction(self, transaction):
        name, amount, location, time = self.parse_transaction(transaction)
        if name not in self.detected_frauds.values():
            self.check_for_frauds(amount, location, name, time)
        self.save_transaction(name, location, time)

    def check_for_frauds(self, amount, location, name, time):
        if self.is_location_and_time_fraud(name, location, time):
            previous_time = self.previous_transaction_time[name]
            self.detected_frauds[previous_time] = name
            return
        if self.is_amount_fraud(amount):
            self.detected_frauds[time] = name

    def is_amount_fraud(self, amount):
        return amount > self.amount_fraud_limit

    def is_location_and_time_fraud(self, name, location, time):
        if name in self.previous_transaction_city.keys() and name in self.previous_transaction_time.keys():
            if self.previous_transaction_city[name] != location:
                if time - self.previous_transaction_time[name] < self.time_fraud_limit:
                    return True
        return False

    def save_transaction(self, name, location, time):
        self.previous_transaction_city[name] = location
        self.previous_transaction_time[name] = time

    @staticmethod
    def sort_by_detection_time(detected_frauds):
        return [detected_frauds[time] for time in sorted(detected_frauds.keys())]
