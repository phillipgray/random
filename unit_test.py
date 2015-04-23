import unittest

def add_1(x):
	return x + 1

class MyTest(unittest.TestCase):
	def test(self):
		self.assertEqual(add_1(1), 2)

if __name__ == '__main__':
    unittest.main()