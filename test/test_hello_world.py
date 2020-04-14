import unittest
from main_source import hello_world


class mytestcase(unittest.TestCase):
    def test_hello_message(self):
        self.assertEqual("Hello,CIS 189!",hello world.hello_message())


if __name__=='maine__':
     unittest.main()