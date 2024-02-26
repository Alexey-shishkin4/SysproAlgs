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
with open('tests/test5', 'r', encoding='utf-8') as file:
    test_cases['500x500'] = eval(file.read())


def test_alg(functions, test_cases):
    res = [[], [], [], [], []]
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
format_table(["128x128", "256x256", "512x512", "1024x1024", "500x500"],
             ["Trivial Multiplication", "Recursive Multiplication", "Strassen Multiplication"],
             res)
print()

with open("test.txt", "r", encoding='utf-8') as file:
    data = eval(file.read())


"""
Benchmark| Trivial Multiplication | Recursive Multiplication | Strassen Multiplication |
|--------------------------------------------------------------------------------------|
128x128  | 0.15473103523254395    | 0.0019996166229248047    | 0.0030078887939453125   |
256x256  | 1.3160440921783447     | 0.017412424087524414     | 0.04616832733154297     |
512x512  | 12.496443271636963     | 0.17498469352722168      | 0.5274195671081543      |
1024x1024| 121.54719042778015     | 1.4747910499572754       | 3.746706962585449       |
500x500  | 12.706296682357788     | 0.1467134952545166       | 0.640181303024292       |
"""