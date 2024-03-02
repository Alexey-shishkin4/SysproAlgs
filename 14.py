from random import randint


def kth(coords, k):
    if len(coords) == 1:
        return coords[0]
    pivot = randint(0, len(coords) - 1)
    p = partition(coords, pivot)

    if p + 1 == k:
        return coords[p + 1]
    elif p + 1 > k:
        return kth(coords[:p + 1], k)
    else:
        return kth(coords[p + 1:], k - p - 1)


def partition(arr, pivot_index):
    n = len(arr) - 1
    pivot_value = arr[pivot_index][1]
    arr[pivot_index], arr[n] = arr[n], arr[pivot_index]
    store_index = 0
    for i in range(n):
        if arr[i][1] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[n] = arr[n], arr[store_index]
    return store_index


arr = [(1, 1), (7, 2), (3, 2), (6, 3), (5, 1)]
# (1,1) (3, 2) (5, 1) (6, 3) (7, 2) медиана: (5, 1) суммарное расстояние 7(по горизонтали) + 4 (по вертикали)
# (1, 1) (5, 1) (3, 2) (7, 2) (6, 3) медина: (3, 2) суммарное расстояние 7 + 3
median = kth(arr, len(arr) // 2)
print("Прямая: y =", median[1])
