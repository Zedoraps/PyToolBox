class Notenrechner:

    def __init__(self, max_points):
        self.max_points = max_points
        self.notenliste = []

    def calculate(self, reached_points):
        resultat = reached_points / self.max_points * 5 + 1
        self.notenliste.append(resultat)
        return resultat

    def average(self):
        average = sum(self.notenliste) / len(self.notenliste)
        return average

    def best(self):
        best = max(self.notenliste)
        return best

    def worst(self):
        worst = min(self.notenliste)
        return worst

    def history(self):
        return self.notenliste
