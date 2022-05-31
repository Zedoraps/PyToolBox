import random


class Zufallswuerfel:

    def __init__(self, maxseiten):
        self.maxseiten = maxseiten
        self.history = []

    def throw(self):
        resultat = random.randint(1, self.maxseiten)
        self.history.append(resultat)
        return resultat

    def get_last_throws(self):
        result = self.history
        result.reverse()
        return result
