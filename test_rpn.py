import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	
	def test_sub(self):
		result = rpn.calculate('4 3 -')
		self.assertEqual(1, result)

	def test_mul(self):
		result = rpn.calculate('4 3 *')
		self.assertEqual(12, result)

	def test_div(self):
		result = rpn.calculate('4 2 /')
		self.assertEqual(2, result)

	def test_chain(self):
		result = rpn.calculate('1 1 + 2 *')
		self.assertEqual(4, result)

	def test_expo(self):
		result = rpn.calculate('2 5 ^')
		self.assertEqual(32, result)
		result = rpn.calculate('3 3 ^')
		self.assertEqual(27, result)




