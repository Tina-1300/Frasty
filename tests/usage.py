import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from Frasty.Fraction import Fraction

# Création de fractions
f1 = Fraction(3, 5)
f2 = Fraction(4, 3)
f3 = Fraction(-2, 7)
f4 = Fraction(6, 8) # va être simplifier à 3/4

print("Fractions cree :")
print(f"f1 = {f1}") 
print(f"f2 = {f2}")
print(f"f3 = {f3}")
print(f"f4 = {f4} (simplifier)")

print("\nRepresentation officielle (repr) :")
print(repr(f1))
print(repr(f4))

# Opérations arithmétiques
print("\nOperations arithmetiques :")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")

# Opérations avec entier
print("\nAvec des entiers :")
print(f"f1 + 2 = {f1 + 2}")
print(f"2 + f1 = {2 + f1}")
print(f"f1 * 3 = {f1 * 3}")
print(f"3 * f1 = {3 * f1}")
print(f"f1 - 1 = {f1 - 1}")
print(f"1 - f1 = {1 - f1}")
print(f"f1 / 2 = {f1 / 2}")
print(f"2 / f1 = {2 / f1}")

# Comparaisons
print("\nComparaisons :")
print(f"f1 == Fraction(3,5) ? {f1 == Fraction(3,5)}")  # True
print(f"f1 == f2 ? {f1 == f2}")  # False
print(f"f1 != f2 ? {f1 != f2}")  # True
print(f"f1 < f2 ? {f1 < f2}") # True
print(f"f1 <= Fraction(3,5) ? {f1 <= Fraction(3,5)}") # True
print(f"f1 > f3 ? {f1 > f3}") # True
print(f"f1 >= Fraction(1,2) ? {f1 >= Fraction(1,2)}") # True

# Comparaisons avec entiers
print("\nComparaisons avec entiers :")
print(f"f1 == 6 ? {f1 == 6}") 
print(f"f1 < 1 ? {f1 < 1}")
print(f"f1 <= 2 ? {f1 <= 2}") 
print(f"f1 > 0 ? {f1 > 0}")
print(f"f1 >= 2 ? {f1 >= 2}")

# Vérification addition et égalité
print("\nTest egalite apres addition :")
if f1 + f2 == Fraction(29, 15):
    print(f"{f1} + {f2} = 29/15 (correct)")

# This method returns the value of a fraction in decimal
print(Fraction(14, 6).display_the_value_in_decimal()) # 2.3333333333333335
print(Fraction(13, 8).display_the_value_in_decimal()) # 1.625
