import unittest
from code42 import ImplicitTreap
import random


class TestImplicitTreap(unittest.TestCase):
    def setUp(self):
        self.treap = ImplicitTreap()

    def test_insert_single_node(self):
        # Insert a single node and check its size and sum
        self.treap.insert(10, priority=7)
        self.assertEqual(self.treap.root.key, 10)
        self.assertEqual(self.treap.root.size, 1)
        self.assertEqual(self.treap.root.sum, 10)

    def test_insert_multiple_nodes(self):
        # Insert multiple nodes and check tree properties
        self.treap.insert(10, priority=7)
        self.treap.insert(20, priority=8)
        self.treap.insert(15, priority=5)

        # Check the root node and overall structure
        self.assertEqual(self.treap.root.size, 3)  # Total size should be 3
        total_sum = self.treap.get_sum(self.treap.root)
        self.assertEqual(total_sum, 10 + 20 + 15)

    def test_remove_node(self):
        # Insert nodes and remove one
        self.treap.insert(10, priority=7)
        self.treap.insert(20, priority=8)
        self.treap.insert(15, priority=5)

        # Remove a node
        self.treap.remove(15)

        # Check the updated tree structure
        self.assertEqual(self.treap.root.size, 2)  # Total size should now be 2
        remaining_sum = self.treap.get_sum(self.treap.root)
        self.assertEqual(remaining_sum, 10 + 20)

    def test_range_sum(self):
        # Insert nodes and calculate range sum
        self.treap.insert(5, priority=3)
        self.treap.insert(10, priority=7)
        self.treap.insert(15, priority=8)
        self.treap.insert(20, priority=5)
        self.treap.insert(25, priority=6)

        # Calculate the sum of the range [10, 20]
        result = self.treap.range_sum(10, 20)
        self.assertEqual(result, 10 + 15 + 20)

    def test_range_sum_after_remove(self):
        # Insert nodes
        self.treap.insert(5, priority=3)
        self.treap.insert(10, priority=7)
        self.treap.insert(15, priority=8)
        self.treap.insert(20, priority=5)
        self.treap.insert(25, priority=6)

        # Remove a node
        self.treap.remove(15)

        # Calculate the sum of the range [10, 20]
        result = self.treap.range_sum(10, 20)
        self.assertEqual(result, 10 + 20)

    def test_insert_and_remove_all(self):
        # Insert and remove all elements to ensure tree is empty
        keys = [5, 10, 15, 20, 25]
        for key in keys:
            self.treap.insert(key, priority=random.randint(1, 10**9))

        for key in keys:
            self.treap.remove(key)

        # Tree should be empty
        self.assertIsNone(self.treap.root)


if __name__ == "__main__":
    unittest.main()
