import unittest

from cesar import cesar, advanced_cesar


class CesarTestCase(unittest.TestCase):
	def testBasicCase(self):
		self.assertEqual(cesar("A"), "D")
		self.assertEqual(cesar("Z"), "C")

	def testGeneralCase(self):
		for i in range(65, 88):
			self.assertEqual(cesar(chr(i)), chr(i+3))
		for i in range(89, 91):
			self.assertEqual(cesar(chr(i)), chr(i-26+3))

	def testAdvancedCase(self):
		self.assertEqual(advanced_cesar("A", 1), "B")
		self.assertEqual(advanced_cesar("A", 2), "C")
		self.assertEqual(advanced_cesar("A", -1), "Z")
		self.assertEqual(advanced_cesar("B", -1), "A")
		self.assertEqual(advanced_cesar("C", -2), "A")

	def testAdvancedInvertible(self):
		for i in range(1, 26):
			self.assertEqual(advanced_cesar(advanced_cesar("A", i), -i), "A")

	def testAdvancedFullCycle(self):
		for i in range(65, 91):
			self.assertEqual(advanced_cesar(chr(i), 26), chr(i))
			self.assertEqual(advanced_cesar(chr(i), -26), chr(i))

	def testAdvancedMoreCycles(self):
		for i in range(27, 52):
			self.assertEqual(advanced_cesar("A", i), advanced_cesar("A", i-26))
			self.assertEqual(advanced_cesar("A", -i), advanced_cesar("A", -i+26))

if __name__ == '__main__':
	unittest.main()
