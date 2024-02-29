from random import choice


def quicksort_random(nums):
    if len(nums) <= 1:
        return nums
    p = choice(nums)
    left = [i for i in nums if i < p]
    mid = [i for i in nums if i == p]
    right = [i for i in nums if i > p]

    return quicksort_random(left) + mid + quicksort_random(right)


arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort_random(arr))


def lomuto_quicksort(arr, left, right):
    def lomuto_partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if left >= right:
        return arr
    p = lomuto_partition(arr, left, right)
    lomuto_quicksort(arr, left, p - 1)
    lomuto_quicksort(arr, p + 1, right)


def hoara_quicksort(arr, left, right):
    def hoara_partition(arr, low, high):
        pivot = arr[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    if left >= right:
        return arr
    p = hoara_partition(arr, left, right)
    hoara_quicksort(arr, left, p)
    hoara_quicksort(arr, p + 1, right)



arr = [3, 6, 8, 10, 1, 2, 1]
lomuto_quicksort(arr, 0, len(arr) - 1)
print(arr)


arr = [3, 6, 8, 10, 1, 2, 1]
hoara_quicksort(arr, 0, len(arr) - 1)
print(arr)