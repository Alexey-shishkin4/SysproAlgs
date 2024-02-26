import time
from algs import matrix_multi, shtrassen_matrix, recur_matrix_multi


def format_table(benchmarks, algos, results):
    benchmarks.append('Benchmark')
    col_width = [len(max(benchmarks, key=len))]
    for i in range(len(algos)):
        col_width.append(len(max((algos[i], *[str(results[j][i]) for j in range(len(benchmarks[:-1]))]), key=len)))

    print('Benchmark'.ljust(col_width[0]) + '| ' + ' | '.join(str(algos[i]).ljust(col_width[i + 1])
                                                              for i in range(len(algos))) + ' |')
    print('|' + '-' * (sum(col_width) + len(col_width) * 2) + '|')
    for i in range(len(benchmarks[:-1])):
        print(benchmarks[i].ljust(col_width[0]) + '| ' + ' | '.join(str(results[i][j]).ljust(col_width[j + 1])
                                                                    for j in range(len(results[i]))) + ' |')


# Примеры входных данных
test_cases = {
    "Small Matrix": ([
                         [1, 2],
                         [3, 4]
                     ], [
                         [5, 6],
                         [7, 8]
                     ]),
    "Medium Matrix": ([
                          [1, 2, 3, 4],
                          [5, 6, 7, 8],
                          [9, 10, 11, 12],
                          [13, 14, 15, 16]
                      ], [
                          [17, 18, 19, 20],
                          [21, 22, 23, 24],
                          [25, 26, 27, 28],
                          [29, 30, 31, 32]
                      ]),
    "Large Matrix": ([
                         [1, 2, 3, 4, 5, 6, 7, 8],
                         [9, 10, 11, 12, 13, 14, 15, 16],
                         [17, 18, 19, 20, 21, 22, 23, 24],
                         [25, 26, 27, 28, 29, 30, 31, 32],
                         [33, 34, 35, 36, 37, 38, 39, 40],
                         [41, 42, 43, 44, 45, 46, 47, 48],
                         [49, 50, 51, 52, 53, 54, 55, 56],
                         [57, 58, 59, 60, 61, 62, 63, 64]
                     ], [
                         [65, 66, 67, 68, 69, 70, 71, 72],
                         [73, 74, 75, 76, 77, 78, 79, 80],
                         [81, 82, 83, 84, 85, 86, 87, 88],
                         [89, 90, 91, 92, 93, 94, 95, 96],
                         [97, 98, 99, 100, 101, 102, 103, 104],
                         [105, 106, 107, 108, 109, 110, 111, 112],
                         [113, 114, 115, 116, 117, 118, 119, 120],
                         [121, 122, 123, 124, 125, 126, 127, 128]
                     ])

}

def test_alg(functions, test_cases):
    res = [[], [], []]
    c = 0
    for j in test_cases.keys():
        for func in functions:
            start_time = time.time()
            func(*test_cases[j])
            end_time = time.time()
            elapsed_time = end_time - start_time
            res[c].append(elapsed_time)
        c += 1
    return res



funcs = [matrix_multi, recur_matrix_multi, shtrassen_matrix]
res = test_alg(funcs, test_cases)
format_table(["Small Matrix", "Medium Matrix", "Large Matrix"],
             ["Trivial Multiplication", "Recursive Multiplication", "Strassen Multiplication"],
             res)
print()

with open("test.txt", "r", encoding='utf-8') as file:
    data = eval(file.read())

# 512x512
# Trivial
start_time = time.time()
matrix_multi(data, data)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
# Strassen
start_time = time.time()
shtrassen_matrix(data, data)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)