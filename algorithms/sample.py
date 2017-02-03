class PrimeNumberFinder:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.found_primes = [2]

    def find_all_smaller_than_limit(self):
        for candidate in range(self.upper_limit):
            if self.is_prime(candidate):
                self.found_primes.append(candidate)

    def is_prime(self, candidate):
        for previous in self.found_primes:
            if not (candidate // previous) * previous == candidate:
                return False
        return True

    def solve(self):
        self.find_all_smaller_than_limit()
        print(self.found_primes)

a = PrimeNumberFinder(10)

a.solve()

