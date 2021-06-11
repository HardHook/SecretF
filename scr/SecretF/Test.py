import unittest
from main import Full


class Test_secret(unittest.TestCase):

    def test_secret(self):
        a = Full()
        a.secret()
        if a == 0:
            t = False
        else:
            t = True
        self.assertEqual(t, True)

    def test_read(self):
        a = Full()
        a.read()
        if a == '':
            t = False
        else:
            t = True
        self.assertEqual(t, True)


if __name__ == '__main__':
    unittest.main()
