import math
import random


class BloomFilter:
    def __init__(self, n, p):
        self.size = self.calculate_size(n, p)
        self.bit_array = [False] * self.size
        self.num_hashes = self.calculate_hashes(n, self.size)

    def calculate_size(self, n, p):  # m - размер битового массива n - ожидаемое кол-во p - ложно-положит вероятность
        m = - (n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def calculate_hashes(self, n, m):  # кол-во хеш-функций
        k = (m / n) * math.log(2)
        return int(k)

    def hash_functions(self, item):
        random.seed(item)
        return [random.randint(0, self.size - 1) for _ in range(self.num_hashes)]

    def add(self, item):
        hashes = self.hash_functions(item)
        for i in hashes:
            self.bit_array[i] = True

    def __contains__(self, item):
        hashes = self.hash_functions(item)
        for i in hashes:
            if not self.bit_array[i]:
                return False
        return True


total_requests = 1000000  # Прогнозируемое общее количество запросов
desired_error_rate = 0.01  # Желаемая вероятность ошибки

bloom_filter = BloomFilter(total_requests, desired_error_rate)

bloom_filter.add("192.168.0.1")
bloom_filter.add("10.0.0.1")
bloom_filter.add("172.16.0.1")

print("192.168.0.1" in bloom_filter)  # true
print("10.0.0.2" in bloom_filter)    # false
