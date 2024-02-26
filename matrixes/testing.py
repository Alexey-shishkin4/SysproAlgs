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



test_cases = {}
with open('tests/test1', 'r', encoding='utf-8') as file:
    test_cases['128x128'] = eval(file.read())
with open('tests/test2', 'r', encoding='utf-8') as file:
    test_cases['256x256'] = eval(file.read())
with open('tests/test3', 'r', encoding='utf-8') as file:
    test_cases['512x512'] = eval(file.read())
with open('tests/test4', 'r', encoding='utf-8') as file:
    test_cases['1024x1024'] = eval(file.read())


def test_alg(functions, test_cases):
    res = [[], [], [], []]
    c = 0
    for j in test_cases.keys():
        for func in functions:
            start_time = time.time()
            func(test_cases[j], test_cases[j])
            end_time = time.time()
            elapsed_time = end_time - start_time
            res[c].append(elapsed_time)
        c += 1
    return res



funcs = [matrix_multi, recur_matrix_multi, shtrassen_matrix]
res = test_alg(funcs, test_cases)
format_table(["128x128", "256x256", "512x512", "1024x1024"],
             ["Trivial Multiplication", "Recursive Multiplication", "Strassen Multiplication"],
             res)
print()

with open("test.txt", "r", encoding='utf-8') as file:
    data = eval(file.read())


"""
Benchmark| Trivial Multiplication | Recursive Multiplication | Strassen Multiplication |
|--------------------------------------------------------------------------------------|
128x128  | 0.15216803550720215    | 0.0015025138854980469    | 0.0030050277709960938   |
256x256  | 1.2863037586212158     | 0.015727758407592773     | 0.04765653610229492     |
512x512  | 12.264899015426636     | 0.12553095817565918      | 0.46350574493408203     |
1024x1024| 117.94457745552063     | 1.2421700954437256       | 3.7402358055114746      |
"""