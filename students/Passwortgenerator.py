# 25 Zeichen mindestens Informationzeichen
# Zahlen, Sonderzeichen, Klein- und Grosschreibung mindestens einmal
# statt random mit Liste   --> und für Alphabeth und Sonderzeichen mit Liste und Schleifen arbeiten? -->random Liste
# Class: Generator
# print --> return
# sample Funktion
# random.sample(liste, lenge)
# Konsument kann selber wählen wie lang das PW

# gemischt = [7,"a"]
# print (gemischt[:])
# print (gemischt)

from random import *


class PasswortGenerator:
    alphabets = 'abcdefghijklmnopqrstufvwxyzABCDEFGHIJKLMNOPQRSTUFCWXYZ'
    numbers = '0123456789'
    special_characters = "!@#$%^&*()"

    def generieren(self, anzahl, mit_sonderzeichen):
        if mit_sonderzeichen:
            passwort = sample(self.alphabets + self.numbers + self.special_characters, anzahl)
        else:
            passwort = sample(self.alphabets + self.numbers, anzahl)
        return passwort
