import unittest
from random import random, randint

from ssi_lib import mod, add_mod, mul_mod, shift, xor, extended_euclide, gcd, inv_mod, is_prime, is_generator, \
	find_all_generators, generate_prime, exp_mod

"""
Ceci est un fichier qui vous permet de tester votre code Python.
Pour le lancer, il suffit de faire "make test" !
Pour garantir le bon fonctionnement de ce fichier, MERCI DE NE PAS CHANGER CE FICHIER.
"""
class SSILibPartOneTestCase(unittest.TestCase):
	# MOD
	def test_mod_basic_cases(self):
		# Teste les cas de base de mod
		self.assertEqual(mod(1, 10), 1)
		self.assertEqual(mod(3, 10), 3)
		self.assertEqual(mod(10, 10), 0)
		self.assertEqual(mod(11, 10), 1)

	def test_mod_general_cases(self):#from ssi_lib_prof import exp_mod

		# Teste tous les cas de 1 à 34 modulo 17
		for i in range(1, 35):
			self.assertEqual(mod(i, 17), i%17)

	# ADDMOD
	def test_addmod_basic_cases(self):
		self.assertEqual(add_mod(1, 1, 3), 2)
		self.assertEqual(add_mod(1, 0, 3), 1)
		self.assertEqual(add_mod(1, 2, 3), 0)
		self.assertEqual(add_mod(1, 1301, 3), 0)

	def test_addmod_general_cases(self):
		for i in range(1, 18):
			for j in range(1, 18):
				self.assertEqual(add_mod(i, j, 17), (i+j)%17)

	# MULMOD
	def test_mulmod_basic_cases(self):
		self.assertEqual(mul_mod(1, 1, 3), 1)
		self.assertEqual(mul_mod(1, 12, 10), 2)
		self.assertEqual(mul_mod(0, 1, 10), 0)

	def test_mulmod_general_cases(self):
		for i in range(1, 18):
			for j in range(1, 18):
				self.assertEqual(mul_mod(i, j, 17), (i*j)%17)

	# SHIFT
	def test_shift_basic_cases(self):
		# Tests du comportement général
		self.assertEqual(shift(11, 2, 4), 14)
		self.assertEqual(shift(14, 2, 4), 11)
		self.assertEqual(shift(1, 1, 4), 2)
		self.assertEqual(shift(1, 1, 5), 2)
		self.assertEqual(shift(2, 1, 4), 4)
		self.assertEqual(shift(4, 1, 4), 8)
		self.assertEqual(shift(8, 1, 4), 1)
		self.assertEqual(shift(8, 1, 5), 16)
		self.assertEqual(shift(2**15, 1, 16), 1)

	def test_shift_null(self):
		# Si n = 0, alors je ne décale rien.
		self.assertEqual(shift(11, 0, 4), 11)

	def test_shift_full_round(self):
		# Si je décale de length, alors j'ai fait un tour complet.
		self.assertEqual(shift(11, 4, 4), 11)

	def test_shift_more_rounds(self):
		# Si n > length, alors on fait plus d'un tour complet...
		self.assertEqual(shift(11, 6, 4), 14)

	def test_shift_general_cases(self):
		# Teste tous les décalages de 3 positions avec une longueur de 8
		for i in range(1, 256):
			self.assertEqual(shift(i, 3, 8), ((i << 3) + (i >> 5)) & (2**8 - 1))

	# XOR
	def test_xor_fundamental_cases(self):
		self.assertEqual(xor(0, 0), 0)
		self.assertEqual(xor(0, 1), 1)
		self.assertEqual(xor(1, 0), 1)
		self.assertEqual(xor(1, 1), 0)
		self.assertEqual(xor(0, 255), 255)
		self.assertEqual(xor(255, 0), 255)
		self.assertEqual(xor(255, 255), 0)

	def test_xor_invertible(self):
		# XOR est inversible
		self.assertEqual(xor(xor(10, 12), 12), 10)
		self.assertEqual(xor(xor(234, 145), 145), 234)

	def test_xor_general_cases(self):
		for i in range(1, 32):
			for j in range(1, 32):
				self.assertEqual(xor(i, j), i ^ j)

class SSILibPartTwoTestCase(unittest.TestCase):
	# INVMOD
	def test_invmod_basic_cases(self):
		self.assertEqual(inv_mod(14, 23), 5)
		self.assertEqual(inv_mod(4, 17), 13)

		# Si a = 0, on retourne 0
		self.assertEqual(inv_mod(0, 17), 0)
		# Si le PGCD n'est pas 1, on retourne 0
		self.assertEqual(inv_mod(4, 16), 0)

	# PGCD
	def test_gcd_basic_cases(self):
		self.assertEqual(gcd(10, 10), 10)
		self.assertEqual(gcd(141, 255), 3)
		self.assertEqual(gcd(7, 18), 1)

	# EUCLIDE ÉTENDU
	def test_extended_euclide_basic_cases(self):
		# https://www.bibmath.net/crypto/index.php?action=affiche&quoi=complements/algoeuclid
		self.assertEqual(extended_euclide(141, 255), (38, -21))
		self.assertEqual(extended_euclide(10, 3), (1, -3))


class SSILibPartThreeTestCase(unittest.TestCase):
	def test_exp_mod_basic_cases(self):
		self.assertEqual(exp_mod(1, 1, 10), 1)
		self.assertEqual(exp_mod(1, 12, 10), 1)
		self.assertEqual(exp_mod(2, 5, 10), 2)

	def test_exp_mod_advanced_cases(self):
		self.assertEqual(exp_mod(37, 200, 500), 1)
		self.assertEqual(exp_mod(41, 250, 500), 1)
		self.assertEqual(exp_mod(42, 250, 500), 124)

	def test_generate_prime_generates_random_primes(self):
		control_set = set()
		for i in range(20):
			prime = generate_prime(10 ** 4)
			if prime in control_set:
				self.fail("generate_prime is returning the same prime !")
			else:
				control_set.add(prime)

			self.assertEqual(is_prime(prime), True)

	def test_is_prime(self):
		primes = [3307, 2593, 4139, 7829, 4253, 37, 1033]
		non_primes = [25, 40, 90, 144, 42, 8, 2500, 3266, 9999]

		for p in primes:
			self.assertEqual(is_prime(p), True)

		for n in non_primes:
			self.assertEqual(is_prime(n), False)

	def test_is_generator(self):
		Zn = 11
		gens = {k: k in [2, 6, 7, 8] for k in range(1, Zn)}
		for n, prime_check in gens.items():
			self.assertEqual(is_generator(n, Zn), prime_check)

	def test_find_all_generators(self):
		self.assertEqual(find_all_generators(11), [2, 6, 7, 8])
		self.assertEqual(find_all_generators(13), [2, 6, 7, 11])
		self.assertEqual(find_all_generators(17), [3, 5, 6, 7, 10, 11, 12, 14])

if __name__ == '__main__':
	unittest.main()