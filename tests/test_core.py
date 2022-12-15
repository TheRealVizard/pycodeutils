from pycodeutils import *

from unittest import TestCase

class Test(TestCase):
    def setUp(self) -> None:
        self.list = list([1, 2, 3, 4, 5])

    def test_map(self):
        print(self.list.mapped(lambda x: x + 1))
        self.assertListEqual(self.list.mapped(lambda x: x + 1), [2, 3, 4, 5, 6])
