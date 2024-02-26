def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 256

    for i in range(n):
        index = ord(arr[i][exp]) if exp < len(arr[i]) else 0
        count[index] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = ord(arr[i][exp]) if exp < len(arr[i]) else 0
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def lsd_radix_sort(arr):
    max_length = max(len(s) for s in arr)
    for exp in range(max_length - 1, -1, -1):
        counting_sort(arr, exp)


data_to_sort = ["bbb", "aba", "aaa", "aca", "abc", "aaa", "ccc", "hhh"]
print("Исходный массив:")
print(data_to_sort)

# Сортировка с использованием алгоритма поразрядной сортировки
lsd_radix_sort(data_to_sort)
print("Отсортированный массив:")
print(data_to_sort)

# Сравнение с результатом сортировки основанной на сравнении
sorted_comparison = sorted(data_to_sort)
print("Результат сортировки основанной на сравнении:")
print(sorted_comparison)