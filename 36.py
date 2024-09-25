class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size  # оптимизация рангов

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # сжатие пути
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1

    def connected(self, p, q):
        # Проверяем, принадлежат ли элементы одному множеству
        return self.find(p) == self.find(q)


def solution(data: dict):
    sorted_tasks = sorted(data.items(), key=lambda x: -x[1][1])
    uf = UnionFind(len(data) + 1)
    result = []
    bad_tasks = []
    for i, (deadline, penalty) in sorted_tasks:
        available_day = uf.find(deadline)
        if available_day > 0:
            result.append([i, deadline, penalty])
            uf.union(available_day - 1, available_day)
        else:
            bad_tasks.append([i, deadline, penalty])
    return sorted(result, key=lambda x: x[1]), bad_tasks



###TESTS
import unittest


class TestTaskScheduling(unittest.TestCase):

    def test_multiple_tasks(self):
        data = {
            'A': (3, 25),
            'B': (4, 33),
            'C': (1, 40),
            'D': (3, 50),
            'E': (3, 30)
        }
        expected_result = [['C', 1, 40], ['D', 3, 50], ['E', 3, 30], ['B', 4, 33]]
        expected_bad_tasks = [['A', 3, 25]]
        result, bad_tasks = solution(data)
        self.assertEqual(sorted(result, key=lambda x: x[1]), sorted(expected_result, key=lambda x: x[1]))
        self.assertEqual(bad_tasks, expected_bad_tasks)

    def test_all_tasks_can_be_completed(self):
        data = {
            'A': (1, 10),
            'B': (2, 20),
            'C': (3, 30),
            'D': (4, 40),
            'E': (5, 50)
        }
        expected_result = [
            ['A', 1, 10],
            ['B', 2, 20],
            ['C', 3, 30],
            ['D', 4, 40],
            ['E', 5, 50]
        ]
        expected_bad_tasks = []
        result, bad_tasks = solution(data)
        self.assertEqual(sorted(result, key=lambda x: x[1]), sorted(expected_result, key=lambda x: x[1]))
        self.assertEqual(bad_tasks, expected_bad_tasks)

    def test_most_profit_completed(self):
        data = {
            'A': (1, 10),
            'B': (1, 20),
            'C': (1, 30),
        }
        expected_result = [['C', 1, 30]]
        expected_bad_tasks = [['B', 1, 20], ['A', 1, 10]]
        result, bad_tasks = solution(data)
        self.assertEqual(result, expected_result)
        self.assertEqual(bad_tasks, expected_bad_tasks)


if __name__ == '__main__':
    unittest.main()
