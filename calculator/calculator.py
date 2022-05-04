class GradeCalculator:
    max_points = 100

    def __init__(self, max_points):
        self.history = []
        self.max_points = max_points

    def calculate(self, reached_points):
        result = (reached_points * 5) / self.max_points + 1
        self.history.append(result)
        return result

    def highest(self):
        return max(self.history)

    def lowest(self):
        return min(self.history)

    def all(self):
        return self.history

    def avg(self):
        return sum(self.history) / len(self.history)
