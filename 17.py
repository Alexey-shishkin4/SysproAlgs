# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        stack = Stack()
        c = 1
        first, second = head, head
        while first and second:
            if left <= c <= right:
                stack.push(second.val)
                second = second.next
            elif c < left:
                first = first.next
                second = second.next
            elif c > right:
                break
            c += 1
        while first != second:
            first.val = stack.pop()
            first = first.next
        return head


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Test case 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
print("Original linked list:")
print_linked_list(head)
solution.reverseBetween(head, 2, 4)
print("Reversed linked list:")
print_linked_list(head)
# Expected output: 1 -> 4 -> 3 -> 2 -> 5 -> None

# Test case 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
print("Original linked list:")
print_linked_list(head)
solution.reverseBetween(head, 1, 5)
print("Reversed linked list:")
print_linked_list(head)
# Expected output: 5 -> 4 -> 3 -> 2 -> 1 -> None

# Test case 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
print("Original linked list:")
print_linked_list(head)
solution.reverseBetween(head, 1, 3)
print("Reversed linked list:")
print_linked_list(head)
# Expected output: 3 -> 2 -> 1 -> 4 -> 5 -> None

# Test case 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
print("Original linked list:")
print_linked_list(head)
solution.reverseBetween(head, 3, 5)
print("Reversed linked list:")
print_linked_list(head)
# Expected output: 1 -> 2 -> 5 -> 4 -> 3 -> None