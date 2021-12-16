import unittest

class TestString(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isdigit(self):
        self.assertFalse('foo'.isdigit())
    def test_alpha(self):
        self.assertTrue('fo#&~*o'.isascii())

if __name__ == '__main__':
    unittest.main()
