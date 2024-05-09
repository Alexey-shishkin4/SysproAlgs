# insert(val), peek_min(), extract_min(), decrease_key(s, k), merge (h1, h2), delete(s)

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def merge_trees(self, other):
        self, other = sorted([self, other], key=lambda x: x.value)
        self.add_child(other)
        other.parent = self
        return self

    def __len__(self):
        return len(self.children)


class BinomialHeap:
    def __init__(self):
        self.trees = []
        self.min_node = None
        self.count = 0

    def is_empty(self):
        return self.min_node is None

    def insert(self, value):
        node = Node(value)
        new_heap = BinomialHeap()
        new_heap.trees.append(node)
        new_heap.min_node = node
        new_heap.count = 1
        self.merge(new_heap)
        return node

    def peek_min(self):
        return self.min_node

    def extract_min(self):
        min_node = self.min_node
        self.trees.remove(min_node)
        child_heap = BinomialHeap()
        child_heap.trees = min_node.children
        child_heap.count = len(min_node)
        self.merge(child_heap)
        self.count -= 1
        return min_node

    def decrease_key(self, node, new_value):
        if new_value > node.value:
            raise ValueError("New value is greater than current value")
        node.value = new_value
        self._bubble_up(node)

    def merge(self, other_heap):
        new_trees = []
        i, j = 0, 0

        while i < len(self.trees) and j < len(other_heap.trees):
            tree1 = self.trees[i]
            tree2 = other_heap.trees[j]

            if len(tree1) < len(tree2):
                new_trees.append(tree1)
                i += 1
            elif len(tree1) > len(tree2):
                new_trees.append(tree2)
                j += 1
            else:
                merged_tree = tree1.merge_trees(tree2)
                new_trees.append(merged_tree)
                i += 1
                j += 1

        while i < len(self.trees):
            new_trees.append(self.trees[i])
            i += 1

        while j < len(other_heap.trees):
            new_trees.append(other_heap.trees[j])
            j += 1

        self.trees = new_trees
        self.count += other_heap.count
        self._find_min()

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self._find_min()
        self.extract_min()

    def _find_min(self):
        self.min_node = None
        for tree in self.trees:
            if self.min_node is None or tree.value < self.min_node.value:
                self.min_node = tree

    def _bubble_up(self, node):
        parent = node.parent
        while parent is not None and node.value < parent.value:
            node.value, parent.value = parent.value, node.value

    def __len__(self):
        return self.count


def test_insert_and_extract_min():
    heap = BinomialHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert heap.extract_min().value == 3
    assert heap.extract_min().value == 5
    assert heap.extract_min().value == 7
    assert heap.is_empty()


def test_peek_min():
    heap = BinomialHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert heap.peek_min().value == 3


def test_decrease_key():
    heap = BinomialHeap()
    node1 = heap.insert(5)
    heap.insert(3)
    heap.decrease_key(node1, 2)
    assert heap.peek_min().value == 2
    assert heap.extract_min().value == 2
    assert heap.extract_min().value == 3


def test_delete():
    heap = BinomialHeap()
    node1 = heap.insert(5)
    heap.insert(3)
    heap.delete(node1)
    assert heap.peek_min().value == 3
    assert heap.extract_min().value == 3
    assert heap.is_empty()


def test_merge():
    heap1 = BinomialHeap()
    heap2 = BinomialHeap()
    heap1.insert(1)
    heap1.insert(3)
    heap2.insert(2)
    heap2.insert(4)
    heap1.merge(heap2)
    assert heap1.extract_min().value == 1
    assert heap1.extract_min().value == 2
    assert heap1.extract_min().value == 3
    assert heap1.extract_min().value == 4
    assert heap1.is_empty()


test_insert_and_extract_min()
test_peek_min()
test_decrease_key()
test_delete()
test_merge()

print("All tests passed!")