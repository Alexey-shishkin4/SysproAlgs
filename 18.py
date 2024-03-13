from structures import Stack


def get_priority(op):
    priorities = {
        '(': 0,
        ')': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '&': 3,
        '|': 3,
        '^': 3,
        '<<': 4,
        '>>': 4,
        '<': 5,
        '<=': 5,
        '>': 5,
        '>=': 5,
        '==': 6,
        '!=': 6,
        '&&': 7,
        '||': 8,
        '!': 9,
        '~': 9
    }
    return priorities[op]


def is_operator(token):
    operators = ['+', '-', '*', '/', '%', '&', '|', '^', '<<', '>>', '<', '<=', '>', '>=', '==', '!=', '&&', '||', '!', '~']
    return token in operators


def infix_to_rpn(expression):
    output = []
    stack = Stack()

    for i in expression:
        if i.isdigit():
            output.append(i)
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(i):
            while not stack.is_empty() and get_priority(stack.peek()) >= get_priority(i):
                output.append(stack.pop())
            stack.push(i)

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


"""infix_expression = "3 + 14"
print(infix_expression)
print(infix_to_rpn(infix_expression))
"""


def test_infix_to_rpn():
    assert infix_to_rpn("5 + 3 * 7") == "5 3 7 * +"
    assert infix_to_rpn("5 + (3 * 7)") == "5 3 7 * +"
    assert infix_to_rpn("(5 + 3) * 7") == "5 3 + 7 *"
    assert infix_to_rpn("5 * (3 + 7)") == "5 3 7 + *"
    assert infix_to_rpn("5 * (3 + 7) / 2") == "5 3 7 + * 2 /"
    assert infix_to_rpn("(5 * 3 + 7) / 2") == "5 3 * 7 + 2 /"
    assert infix_to_rpn("5 * ((3 + 7) / 2)") == "5 3 7 + 2 / *"
    assert infix_to_rpn("5 & (3 | 7)") == "5 3 7 | &"
    assert infix_to_rpn("5 | (3 & 7)") == "5 3 7 & |"
    assert infix_to_rpn("!5 | (3 & 7)") == "5 ! 3 7 & |"

    print("All tests passed successfully!")


test_infix_to_rpn()
