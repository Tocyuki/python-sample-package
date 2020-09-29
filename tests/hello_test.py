import unittest
from src.sample.hello import *
from src.sample.hello2 import *


class TestSample(unittest.TestCase):
    def test_hello(self):
        actual = hello()
        self.assertEqual('Hello World', actual)


    def test_hello2(self):
        actual = hello2()
        self.assertEqual('Hello World 2', actual)


if __name__ == '__main__':
    unittest.main()
