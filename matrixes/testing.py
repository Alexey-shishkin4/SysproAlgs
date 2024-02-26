import time
import numpy as np
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


def test_alg(functions, test_cases):
    res = [[], [], []]
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


"""funcs = [matrix_multi, recur_matrix_multi, shtrassen_matrix]
for i in range(5):
    res = test_alg(funcs, test_cases)
    format_table(["128x128", "256x256", "512x512"],
                 ["Trivial Multiplication", "Recursive Multiplication", "Strassen Multiplication"],
                 res)"""


trivial_times = [[0.17047691345214844, 0.22783350944519043, 0.22488856315612793, 0.22378849983215332, 0.2290210723876953],
                 [1.401606559753418, 1.8000013828277588, 1.801905632019043, 1.8178319931030273, 1.7586309909820557],
                 [16.93664789199829, 17.04375457763672, 16.879972219467163, 18.052043914794922, 16.98537039756775]]
recursive_times = [[0.16545701026916504, 0.24921274185180664, 0.22899389266967773, 0.24831318855285645, 0.21692776679992676],
                   [1.4590415954589844, 1.6289587020874023, 1.6772816181182861, 1.620393991470337, 1.6733098030090332],
                   [13.463587999343872, 13.585960626602173, 13.376194715499878, 13.31449818611145, 16.309454202651978]]
strassen_times = [[0.14446425437927246, 0.16472315788269043, 0.187591552734375, 0.16675233840942383, 0.17537856101989746],
                  [1.3430335521697998, 1.3493385314941406, 1.3859667778015137, 1.3248395919799805, 1.3102126121520996],
                  [9.521635293960571, 9.559378623962402, 9.535282850265503, 9.405028581619263, 11.462777137756348]]


def calculate_statistics(times):
    means = np.mean(times, axis=1)
    std_devs = np.std(times, axis=1)
    geo_means = np.exp(np.mean(np.log(times), axis=1))
    return means, std_devs, geo_means


trivial_means, trivial_std_devs, trivial_geo_means = calculate_statistics(trivial_times)
recursive_means, recursive_std_devs, recursive_geo_means = calculate_statistics(recursive_times)
strassen_means, strassen_std_devs, strassen_geo_means = calculate_statistics(strassen_times)


print("Trivial Multiplication:")
print("Среднее:", trivial_means)
print("Стандартное отклонение:", trivial_std_devs)
print("Среднее геометрическое:", trivial_geo_means)
print()
print("Recursive Multiplication:")
print("Среднее:", recursive_means)
print("Стандартное отклонение:", recursive_std_devs)
print("Среднее геометрическое:", recursive_geo_means)
print()
print("Strassen Multiplication:")
print("Среднее:", strassen_means)
print("Стандартное отклонение:", strassen_std_devs)
print("Среднее геометрическое:", strassen_geo_means)


"""
Benchmark| Trivial Multiplication | Recursive Multiplication | Strassen Multiplication |
|--------------------------------------------------------------------------------------|
128x128  | 0.17047691345214844    | 0.16545701026916504      | 0.14446425437927246     |
256x256  | 1.401606559753418      | 1.4590415954589844       | 1.3430335521697998      |
512x512  | 16.93664789199829      | 13.463587999343872       | 9.521635293960571       |
Benchmark| Trivial Multiplication | Recursive Multiplication | Strassen Multiplication |
|--------------------------------------------------------------------------------------|
128x128  | 0.22783350944519043    | 0.24921274185180664      | 0.16472315788269043     |
256x256  | 1.8000013828277588     | 1.6289587020874023       | 1.3493385314941406      |
512x512  | 17.04375457763672      | 13.585960626602173       | 9.559378623962402       |
Benchmark| Trivial Multiplication | Recursive Multiplication | Strassen Multiplication |
|--------------------------------------------------------------------------------------|
128x128  | 0.22488856315612793    | 0.22899389266967773      | 0.187591552734375       |
256x256  | 1.801905632019043      | 1.6772816181182861       | 1.3859667778015137      |
512x512  | 16.879972219467163     | 13.376194715499878       | 9.535282850265503       |
Benchmark| Trivial Multiplication | Recursive Multiplication | Strassen Multiplication |
|--------------------------------------------------------------------------------------|
128x128  | 0.22378849983215332    | 0.24831318855285645      | 0.16675233840942383     |
256x256  | 1.8178319931030273     | 1.620393991470337        | 1.3248395919799805      |
512x512  | 16.98537039756775      | 13.31449818611145        | 9.405028581619263       |
Benchmark| Trivial Multiplication | Recursive Multiplication | Strassen Multiplication |
|--------------------------------------------------------------------------------------|
128x128  | 0.2290210723876953     | 0.21692776679992676      | 0.17537856101989746     |
256x256  | 1.7586309909820557     | 1.6733098030090332       | 1.3102126121520996      |
512x512  | 18.052043914794922     | 16.309454202651978       | 11.462777137756348      |
"""
