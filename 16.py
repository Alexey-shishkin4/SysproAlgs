class LinkedList:
    class Node:
        def __init__(self, val, nxt=None, idx=0):
            self.val = val
            self.next = nxt
            self.idx = idx

        def __str__(self):
            return str((self.val, self.idx))

    def __init__(self):
        self.head = self.tail = None

    def add_to_tail(self, val):
        if isinstance(val, LinkedList.Node):
            node = val
        else:
            node = LinkedList.Node(val)
        if self.tail:
            node.idx = self.tail.idx + 1
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node


lst = LinkedList()
lst.add_to_tail(3)
lst.add_to_tail(2)
lst.add_to_tail(0)
lst.add_to_tail(-4)
lst.add_to_tail(lst.head.next)

def solution(head):
    first, second = head, head
    flag = False
    while second and second.next:
        second = second.next.next
        first = first.next
        if first == second:
            flag = True
            break

    if not flag:
        return None

    # расстояние от головы до начала цикла = расстоянию от встречи до начала цикла
    first = head
    while first != head:
        first = first.next
        second = second.next
    return first



print(solution(lst.head))