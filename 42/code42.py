import random


class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.size = 1
        self.sum = key
        self.left = None
        self.right = None


class ImplicitTreap:
    def __init__(self):
        self.root = None

    def get_size(self, node):
        return node.size if node else 0

    def get_sum(self, node):
        return node.sum if node else 0

    def update(self, node):
        if node:
            node.size = 1 + self.get_size(node.left) + self.get_size(node.right)
            node.sum = node.key + self.get_sum(node.left) + self.get_sum(node.right)

    def split(self, T, key):
        if not T:
            return None, None
        if key > T.key:
            RL, RR = self.split(T.right, key)
            T.right = RL
            self.update(T)
            return T, RR
        else:
            LL, LR = self.split(T.left, key)
            T.left = LR
            self.update(T)
            return LL, T

    def merge(self, T1, T2):
        if not T1:
            return T2
        if not T2:
            return T1
        if T1.priority > T2.priority:
            T1.right = self.merge(T1.right, T2)
            self.update(T1)
            return T1
        else:
            T2.left = self.merge(T1, T2.left)
            self.update(T2)
            return T2

    def insert(self, key, priority=None):
        if priority is None:
            priority = random.randint(1, 10**9)
        new_node = Node(key, priority)
        T1, T2 = self.split(self.root, key)
        self.root = self.merge(self.merge(T1, new_node), T2)

    def remove(self, key):
        T1, T2 = self.split(self.root, key)
        if T2:
            target, T2 = self.split(T2, key + 1)
        self.root = self.merge(T1, T2)

    def range_sum(self, left, right):
        T1, middle = self.split(self.root, left)
        middle, T2 = self.split(middle, right + 1)
        result = self.get_sum(middle)
        self.root = self.merge(self.merge(T1, middle), T2)
        return result


"""treap = ImplicitTreap()
treap.insert(10, 7)
treap.insert(20, 8)
treap.insert(15, 5)

print("Sum of [10, 20]:", treap.range_sum(10, 20))

treap.remove(15)
print("Sum of [10, 20]:", treap.range_sum(10, 20))
"""