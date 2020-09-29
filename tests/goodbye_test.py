import unittest
from src.sample2.goodbye import *
from src.sample2.goodbye2 import *


class TestSample2(unittest.TestCase):
    def test_goodbye(self):
        actual = goodbye()
        self.assertEqual('Good Bye', actual)


    def test_goodbye2(self):
        actual = goodbye2()
        self.assertEqual('Good Bye 2', actual)


if __name__ == '__main__':
    unittest.main()
