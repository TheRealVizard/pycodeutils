from unittest import TestCase

from pycodeutils import *


class Test(TestCase):
    def setUp(self) -> None:
        self.list = list([1, 2, 3, 4, 5])
        self.set = set([1, 2, 3, 4])

    def test_map(self):
        self.assertListEqual(self.list.mapped(lambda x: x + 1), [2, 3, 4, 5, 6])

    def test_set(self):
        new_set = self.set + [1, 5, 6, 7]
        self.assertEqual(len(new_set), 7)
        new_set = new_set + set([8, 6, 7])
        self.assertEqual(len(new_set), 8)
        new_set = self.set + 10
        self.assertEqual(len(new_set), 5)
