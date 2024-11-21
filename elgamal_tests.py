import os
import unittest

from elgamal import write_keys, load_keys, generate_keys, sign, verify
from ssi_lib import is_prime, is_generator, exp_mod, add_mod


class ElGamalTestCase(unittest.TestCase):
	@staticmethod
	def __clean__():
		"""
		Ceci n'est pas un test : cette méthode permet de nettoyer les fichiers qui vont
		altérer le fonctionnement de votre code.
		"""
		to_delete = ["key", "key.pub", "message_signed.txt"]
		try:
			for file in to_delete:
				os.remove(file)
		except FileNotFoundError:
			pass

	def setUp(self):
		self.__clean__()

	def tearDown(self):
		self.__clean__()

	def test_write_key_works_properly(self):
		# Ce test valide le bon fonctionnement de la sérialisation sous forme de clé.
		a, p, g, A = 0, 1, 2, 3
		write_keys(a, p, g, A)

		with open("key.pub") as pub:
			self.assertEqual(pub.readline().strip(), str(p))
			self.assertEqual(pub.readline().strip(), str(g))
			self.assertEqual(pub.readline().strip(), str(A))

		with open("key") as priv:
			self.assertEqual(priv.read(), str(a))

	def test_load_keys_works_properly(self):
		a, p, g, A = 0, 1, 2, 3
		write_keys(a, p, g, A)

		p1, g1, A1, a1 = load_keys()
		# Clé publique
		self.assertEqual(p, p1)
		self.assertEqual(g, g1)
		self.assertEqual(A, A1)
		# Clé privée
		self.assertEqual(a, a1)

	def test_generate_key(self):
		p, g, A, a = generate_keys()
		# On teste les différentes variables pour vérifier qu'elles ont des contraintes satisfaisantes.
		# Les contraintes sont décrites dans l'énoncé.

		# Est-ce que p est premier ?
		self.assertEqual(is_prime(p), True)
		# Est-ce que a est entre 0 et p-1 (0 compris) ?
		self.assertEqual(0 <= a < p - 1, True)
		# Est-ce que g est bien générateur mod p ?
		self.assertEqual(is_generator(g, p), True)
		# Est-ce que A est modulo de p ? Est-ce que A est bien g ** a mod p ?
		self.assertEqual(A < p, True)
		self.assertEqual(exp_mod(g, a, p) == A, True)

	def test_verify_works_with_sign(self):
		# Ce test
		p, g, A, a = generate_keys()
		message = int.from_bytes("Test".encode())
		Y, S = sign(message, p, a, g)

		# Signature valide
		self.assertEqual(verify(message, A, Y, S, g, p), True)

		# Signature invalide
		self.assertEqual(verify(message, A, add_mod(Y, 1, p), S, g, p), False)
		self.assertEqual(verify(message, A, Y, add_mod(S, 1, p - 1), g, p), False)

if __name__ == '__main__':
	unittest.main()
