class PersistentSegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.versions = []
        self.data = data
        self.root = self.build(0, self.n - 1)
        self.versions.append(self.root)

    def build(self, l, r):
        if l == r:
            return Node(count=0)
        mid = (l + r) // 2
        left_child = self.build(l, mid)
        right_child = self.build(mid + 1, r)
        return Node(left=left_child, right=right_child, count=0)

    def update(self, prev_root, idx):
        def update_node(node, l, r):
            if l == r:
                return Node(left=None, right=None, count=node.count + 1)
            mid = (l + r) // 2
            if idx <= mid:
                left_child = update_node(node.left, l, mid)
                return Node(left=left_child, right=node.right, count=node.count + 1)
            else:
                right_child = update_node(node.right, mid + 1, r)
                return Node(left=node.left, right=right_child, count=node.count + 1)

        new_root = update_node(prev_root, 0, self.n - 1)
        self.versions.append(new_root)

    def query(self, version_l, version_r, ql, qr):
        def query_node(node_l, node_r, l, r):
            if qr < l or ql > r:
                return 0
            if ql <= l and r <= qr:
                return node_r.count - node_l.count
            mid = (l + r) // 2
            left_result = query_node(node_l.left, node_r.left, l, mid) if node_l and node_r else 0
            right_result = query_node(node_l.right, node_r.right, mid + 1, r) if node_l and node_r else 0
            return left_result + right_result

        return query_node(version_l, version_r, 0, self.n - 1)

    def build_persistent_tree(self):
        indexed_data = sorted(((val, idx) for idx, val in enumerate(self.data)), reverse=True)
        for _, idx in indexed_data:
            self.update(self.versions[-1], idx)


class Node:
    def __init__(self, left=None, right=None, count=0):
        self.left = left
        self.right = right
        self.count = count


data = [1, 5, 2, 4, 3]
tree = PersistentSegmentTree(data)

tree.build_persistent_tree()

version_l = tree.versions[0]
version_r = tree.versions[-1]
print(tree.query(version_l, version_r, 1, 4))  # 4


data = [1, 3, 5, 7, 9]
tree = PersistentSegmentTree(data)

# Query for updates in the range [1, 4] before any updates have been made
version_l = tree.versions[0]
version_r = tree.versions[0]  # Same version as there have been no updates
print(tree.query(version_l, version_r, 1, 4))  # 0


data = [100, 200, 300, 400, 500]
tree = PersistentSegmentTree(data)

# Perform updates at various indices
tree.update(tree.versions[-1], 1)  # Update index 1
tree.update(tree.versions[-1], 3)  # Update index 3
tree.update(tree.versions[-1], 4)  # Update index 4

# Query for the number of updates in the range [0, 4] between the first and last version
version_l = tree.versions[0]
version_r = tree.versions[-1]
print(tree.query(version_l, version_r, 0, 4))  # 3


data = [10, 30, 20, 50, 40]
tree = PersistentSegmentTree(data)

# Build the persistent tree with all updates based on sorted values
tree.build_persistent_tree()

# Query the number of updates between two versions for the range [1, 3]
version_l = tree.versions[0]
version_r = tree.versions[-1]
print(tree.query(version_l, version_r, 1, 3))  # 3


data = [3, 6, 9, 12, 15]
tree = PersistentSegmentTree(data)

# Perform updates at different indices
tree.update(tree.versions[-1], 1)  # Update index 1
tree.update(tree.versions[-1], 2)  # Update index 2
tree.update(tree.versions[-1], 4)  # Update index 4

# Query the number of updates in the range [2, 4] between the initial and latest version
version_l = tree.versions[0]
version_r = tree.versions[-1]
print(tree.query(version_l, version_r, 2, 4))  # 2
