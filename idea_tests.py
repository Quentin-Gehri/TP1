import unittest

from idea import generate_subkeys, full_round, half_round, encrypt, decrypt, pad, group

class IDEATestCase(unittest.TestCase):
	def test_key_generation_returns_the_good_amount_of_subkeys(self):
		key = "11011100011011110011111101011001"
		subkeys = generate_subkeys(key)

		self.assertEqual(5, len(subkeys))
		for i in range(4):
			self.assertEqual(6, len(subkeys[i]))

		self.assertEqual(4, len(subkeys[-1]))

	def test_key_generation_simple_pattern(self):
		# U = 0b01010101. Vu que la génération n'est que des shifts, on peut vite la tester.
		# Qui plus est, le décalage cyclique de 01010101 << 6 est... lui-même :)
		# On peut considérer ce test comme la fonction identité.
		key = "01010101010101010101010101010101"
		expected_key = [[5] * 6, [5] * 6, [5] * 6, [5] * 6, [5, 5, 5, 5]]

		self.assertEqual(generate_subkeys(key), expected_key)

	def test_key_generation_works_properly(self):
		key = "11011100011011110011111101011001"
		expected_subkeys = [
			[13, 12, 6, 15, 3, 15],
			[5, 9, 1, 11, 12, 15],
			[13, 6, 7, 7, 15, 3],
			[15, 5, 9, 13, 12, 6],
			[15, 13, 6, 7]
		]

		subkeys = generate_subkeys(key)
		self.assertEqual(subkeys, expected_subkeys)

	def test_single_encryption_round(self):
		key = "11011100011011110011111101011001"
		message = "1001110010101100"
		expected = [7, 11, 8, 9]

		# Formatting so that we can actually call full_round
		message_blocks_bin = [message[i:i + 4] for i in range(0, len(message), 4)]
		message_blocks = [int(m, 2) for m in message_blocks_bin]
		key_blocks = generate_subkeys(key)

		# Let's go
		one_round = full_round(message_blocks, key_blocks[0])
		self.assertEqual(expected, one_round)

	def test_multiple_encryption_round(self):
		key = "11011100011011110011111101011001"
		message = "1001110010101100"
		expected = [
			[7, 11, 8, 9],
			[6, 6, 14, 12],
			[4, 14, 11, 2],
			[3, 14, 14, 4]
		]

		# Formatting so that we can actually call full_round
		message_blocks_bin = [message[i:i + 4] for i in range(0, len(message), 4)]
		message_blocks = [int(m, 2) for m in message_blocks_bin]
		subkeys = generate_subkeys(key)

		# Let's go
		for i in range(4):
			message_blocks = full_round(message_blocks, subkeys[i])
			self.assertEqual(expected[i], message_blocks)

	def test_half_encryption_round(self):
		key = "11011100011011110011111101011001"
		message = "0011111011100100"

		# Formatting so that we can actually call full_round
		message_blocks_bin = [message[i:i + 4] for i in range(0, len(message), 4)]
		message_blocks = [int(m, 2) for m in message_blocks_bin]
		key_blocks = generate_subkeys(key)

		self.assertEqual(half_round(message_blocks, key_blocks[-1]), [11, 11, 4, 11])

	def test_full_encryption(self):
		key = "11011100011011110011111101011001"
		message = "1001110010101100"
		expected_cipher = "1011101101001011"

		subkeys = generate_subkeys(key)
		cipher = encrypt(message, subkeys)

		self.assertEqual(cipher, expected_cipher)

	def test_single_decryption_round(self):
		subkeys_round_zero = [8, 3, 10, 5, 12, 6]
		message = "1011101101001011"
		expected = [9, 3, 4, 9]

		# Formatting so that we can actually call full_round
		message_blocks_bin = [message[i:i + 4] for i in range(0, len(message), 4)]
		message_blocks = [int(m, 2) for m in message_blocks_bin]

		# Let's go
		one_round = full_round(message_blocks, subkeys_round_zero)
		self.assertEqual(expected, one_round)

	def test_multiple_decryption_round(self):
		message = "1011101101001011"
		subkeys = [
			[8, 3, 10, 5, 12, 6],
			[8, 11, 7, 4, 15, 3],
			[4, 10, 9, 5, 12, 15],
			[7, 7, 15, 14, 3, 15],
			[4, 4, 10, 8]
		]
		expected = [
			[9, 3, 4, 9], [10, 12, 5, 0], [1, 4, 9, 14], [15, 8, 0, 10], [9, 12, 10, 12],
		]

		# Formatting so that we can actually call full_round
		message_blocks_bin = [message[i:i + 4] for i in range(0, len(message), 4)]
		message_blocks = [int(m, 2) for m in message_blocks_bin]

		# Let's go
		for i in range(4):
			message_blocks = full_round(message_blocks, subkeys[i])
			self.assertEqual(expected[i], message_blocks)

	def test_decryption_is_inverse_of_encryption(self):
		key = "11011100011011110011111101011001"
		message = "1001110010101100"
		subkeys = generate_subkeys(key)
		cipher = encrypt(message, subkeys)
		cleartext = decrypt(cipher, subkeys)

		self.assertEqual(cleartext, message)

	def test_bonus_padding(self):
		message = "10101010"
		self.assertEqual(message + '00100000', pad(message))

	def test_bonus_grouping(self):
		message = "10101010" * 10
		self.assertEqual(["10101010" * 2] * 5, group(message))

	def test_bonus_encryption(self):
		# Je chiffre un texte plus long que 16 bits. J'aimerais voir si on arrive à le chiffrer correctement.
		# Essayez de retrouver la vidéo en question!
		message = ("011010000111010001110100011100000111001100111010001011110010111101111001011011110111010101110"
		           "100011101010010111001100010011001010010111100110110001011010100010101001110011110000011011001"
		           "00111101000001011010110110011001110011")
		key = "11011100011011110011111101011001"
		# On commence à préparer les sous-clés
		subkeys = generate_subkeys(key)

		groups = group(pad(message))
		output = "".join([encrypt(grp, subkeys) for grp in groups])
		cipher = ("0000100111011110100010011110001011101011111001010110101100111101111001100101010100000101011010"
		          "0000100111010001010010000011011111001001000100001110110011111100111010010010011111101111010000"
		          "010000111101010000011110100111100110")

		self.assertEqual(output, cipher)

	def test_bonus_decryption(self):
		cipher = ("0000100111011110100010011110001011101011111001010110101100111101111001100101010100000101011010"
		          "0000100111010001010010000011011111001001000100001110110011111100111010010010011111101111010000"
		          "010000111101010000011110100111100110")
		key = "11011100011011110011111101011001"
		subkeys = generate_subkeys(key)

		groups = group(cipher)
		output = "".join([decrypt(subcipher, subkeys) for subcipher in groups])
		message = ("011010000111010001110100011100000111001100111010001011110010111101111001011011110111010101110"
		           "100011101010010111001100010011001010010111100110110001011010100010101001110011110000011011001"
		           "00111101000001011010110110011001110011")
		self.assertEqual(message, output)

if __name__ == '__main__':
	unittest.main()
