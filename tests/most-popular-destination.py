class Solution:
    def __init__(self, number_of_queries):
        self.number_of_queries = number_of_queries
        self.queries_map = {}
        self.most_searched_destination = None
        self.most_searched_times = None

    def solve(self):
        for _ in range(self.number_of_queries):
            query, number = self.load_query()
            self.update_most_searched(query, number)
        print(self.most_searched_destination)

    def load_query(self):
        query = input()
        if query in self.queries_map.keys():
            self.queries_map[query] += 1
        else:
            self.queries_map[query] = 1
        return query, self.queries_map[query]

    def update_most_searched(self, query, number_searched):
        if self.most_searched_times is None or number_searched > self.most_searched_times:
            self.most_searched_destination = query
            self.most_searched_times = number_searched


def OutputMostPopularDestination(count):
    solution = Solution(count)
    solution.solve()

OutputMostPopularDestination()
