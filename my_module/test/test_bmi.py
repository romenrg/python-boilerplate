import unittest
from my_module import MyClass

class TestMyModule(unittest.TestCase):
    def test_my_method(self):
        test_my_class = MyClass()
        self.assertEqual(test_my_class.my_method(), "Hello to Romén's Python boilerplate project", "Message should match")
