class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(key=lambda x: x[0])

    def pop(self):
        return self.elements.pop(0)[1]

    def peek(self):
        return self.elements[0][1]

    def is_empty(self):
        return len(self.elements) == 0


def mergeKLists(lists):
    pq = PriorityQueue()

    # добавляем каждый указатель списка в очередь
    for head in lists:
        if head:
            pq.push(head, head.val)

    res = ListNode()
    curr = res

    while not pq.is_empty():
        node = pq.pop()  # по наименьшему приоритету
        curr.next = node
        curr = curr.next

        if node.next:
            pq.push(node.next, node.next.val)

    return res.next


# Вспомогательная функция для преобразования массивов в связанные списки
def arrayToList(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


# Вспомогательная функция для преобразования связанных списков в массивы
def listToArray(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


# Пример использования
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [arrayToList(lst) for lst in lists]
result = mergeKLists(lists)
print(listToArray(result))  # Вывод: [1, 1, 2, 3, 4, 4, 5, 6]
