import sys
import os
import unittest

# python -m unittest test_fraction.py

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from Frasty.Fraction import Fraction

# Test Unitaires
class TestFraction(unittest.TestCase):

    def test_initialization(self):
        # Test de la création de base
        f = Fraction(1, 2)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 2)

        # Test de la simplification
        f_simplified = Fraction(2, 4)
        self.assertEqual(f_simplified.numerator, 1)
        self.assertEqual(f_simplified.denominator, 2)

        f_neg_den = Fraction(1, -2) # Teste le dénominateur négatif
        self.assertEqual(f_neg_den.numerator, -1)
        self.assertEqual(f_neg_den.denominator, 2)

        f_neg_num = Fraction(-1, 2) # Teste le numérateur négatif
        self.assertEqual(f_neg_num.numerator, -1)
        self.assertEqual(f_neg_num.denominator, 2)

        f_double_neg = Fraction(-2, -4) # Teste double négatif
        self.assertEqual(f_double_neg.numerator, 1)
        self.assertEqual(f_double_neg.denominator, 2)

        f_zero_num = Fraction(0, 5) # Teste numérateur zéro
        self.assertEqual(f_zero_num.numerator, 0)
        self.assertEqual(f_zero_num.denominator, 1) # Doit simplifier 0/x à 0/1

    def test_zero_denominator_raises_error(self):
        # Teste que la création avec un dénominateur zéro lève une erreur
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    # --- Tests des opérateurs arithmétiques ---
    def test_add(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(-1, 2) + Fraction(1, 4), Fraction(-1, 4))
        self.assertEqual(Fraction(0, 1) + Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) + 1, Fraction(3, 2)) # Teste avec un entier
        self.assertEqual(1 + Fraction(1, 2), Fraction(3, 2)) # Teste avec un entier (radd)

    def test_sub(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), Fraction(0, 1))
        self.assertEqual(Fraction(1, 4) - Fraction(1, 2), Fraction(-1, 4))
        self.assertEqual(Fraction(1, 2) - 1, Fraction(-1, 2)) # Teste avec un entier
        self.assertEqual(1 - Fraction(1, 2), Fraction(1, 2)) # Teste avec un entier (rsub)


    def test_mul(self):
        self.assertEqual(Fraction(1, 2) * Fraction(1, 3), Fraction(1, 6))
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))
        self.assertEqual(Fraction(0, 1) * Fraction(5, 7), Fraction(0, 1))
        self.assertEqual(Fraction(1, 2) * 2, Fraction(1, 1)) # Teste avec un entier
        self.assertEqual(2 * Fraction(1, 2), Fraction(1, 1)) # Teste avec un entier (rmul)


    def test_truediv(self):
        self.assertEqual(Fraction(1, 2) / Fraction(1, 3), Fraction(3, 2))
        self.assertEqual(Fraction(2, 3) / Fraction(1, 2), Fraction(4, 3))
        self.assertEqual(Fraction(1, 2) / 2, Fraction(1, 4)) # Teste avec un entier
        self.assertEqual(2 / Fraction(1, 2), Fraction(4, 1)) # Teste avec un entier (rtruediv)


    def test_division_by_zero_fraction_raises_error(self):
        # Teste la division par une fraction avec numérateur zéro
        with self.assertRaises(ValueError):
            Fraction(1, 2) / Fraction(0, 5)

    # --- Tests des représentations ---
    def test_str_representation(self):
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(5, 1)), "5/1")
        self.assertEqual(str(Fraction(0, 3)), "0/1") # doit être simplifié

    def test_repr_representation(self):
        self.assertEqual(repr(Fraction(1, 2)), "Fraction(1, 2)")
        self.assertEqual(repr(Fraction(2, 4)), "Fraction(1, 2)") # Repr d'un objet simplifié

    # --- Tests des comparaisons ---
    def test_equality(self):
        self.assertTrue(Fraction(1, 2) == Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4)) # Teste avec simplification
        self.assertFalse(Fraction(1, 2) == Fraction(1, 3))
        self.assertFalse(Fraction(1, 2) == 0.5) # Ne devrait pas être égal à un float

    def test_less_than(self):
        self.assertTrue(Fraction(1, 3) < Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) < Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) < Fraction(1, 3))
        self.assertTrue(Fraction(1, 2) < 1) # Teste avec un entier

    def test_less_than_or_equal(self):
        self.assertTrue(Fraction(1, 3) <= Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) <= Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) <= Fraction(1, 3))
        self.assertTrue(Fraction(1, 2) <= 1) # Vrai
        self.assertFalse(Fraction(1, 2) <= 0) # Faux

    def test_greater_than(self):
        self.assertTrue(Fraction(1, 2) > Fraction(1, 3))
        self.assertFalse(Fraction(1, 2) > Fraction(1, 2))
        self.assertFalse(Fraction(1, 3) > Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) > 0) # Teste avec un entier

    def test_greater_than_or_equal(self):
        self.assertTrue(Fraction(1, 2) >= Fraction(1, 3))
        self.assertTrue(Fraction(1, 2) >= Fraction(1, 2))
        self.assertFalse(Fraction(1, 3) >= Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) >= 0)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)