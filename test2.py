def merge(array, from1, to1, from2, to2, buffer: int):  # [from1, to1] - первый диапазон
    while from1 <= to1 and from2 <= to2:                # [from2, to2] - второй диапазон
        if array[from1] <= array[from2]:                # buffer - начало буферной области
            array[from1], array[buffer] = array[buffer], array[from1]
            from1 += 1
        else:
            array[from2], array[buffer] = array[buffer], array[from2]
            from2 += 1
        buffer += 1

    while from1 <= to1:
        array[from1], array[buffer] = array[buffer], array[from1]
        from1 += 1
        buffer += 1

    while from2 <= to2:
        array[from2], array[buffer] = array[buffer], array[from2]
        from2 += 1
        buffer += 1


def sort_with_buff(arr, start, end, buffer):
    if start >= end:
        arr[start], arr[buffer] = arr[buffer], arr[start]
    else:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, mid + 1, end, buffer)


def merge_sort(arr, start, end):
    if start + 1 == end:
        arr[start], arr[end] = arr[end], arr[start]
    elif start < end:
        mid = (start + end) // 2
        buffer = end - mid - (start + mid + 1) // 2
        sort_with_buff(arr, start, mid, buffer)
        l2 = buffer  # [l1, ..., r1, l2, ..., r2]
        r2 = end
        l1 = start
        r1 = l2 - 1
        while r1 - l1 > 1:
            mid = (l1 + r1) // 2
            length = r1 - mid - 1
            sort_with_buff(arr, mid + 1, r1, length)
            merge(arr, l1, l1 + length - 1, l2, r2, r1 - length + 1)
            r1 = r1 - length
            l2 = r1 + 1
        for i in range(r1, l1):
            j = i + 1
            while j <= end and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]



arr = [6, 2, 3, 1, 7, 4, 9, 5]
merge_sort(arr, 0, len(arr) - 1)
print(arr)