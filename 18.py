from structures import Stack


def get_priority(op):
    priorities = {
        '(': 0,
        ')': 0,
        '+': 1,
        '-': 1,
        '**': 2,
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
        '~': 9,
    }
    return priorities[op]


def is_operator(token):  # << >> <= >= == != && || **
    operators = ['+', '-', '*', '/', '%', '&', '|', '^', '<<', '>>', '<', '<=', '>', '>=', '==', '!=', '&&', '||', '!', '~', '**']
    return token in operators


def infix_to_rpn(expression):
    output = []
    stack = Stack()
    flag = False
    for i in range(len(expression)):
        if flag:
            flag = False
            continue
        if expression[i].isdigit():
            output.append(expression[i])
        elif expression[i] == '(':
            stack.push(expression[i])
        elif expression[i] == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        elif i + 1 < len(expression) and is_operator(expression[i] + expression[i + 1]):
            while not stack.is_empty() and get_priority(stack.peek()) > get_priority(expression[i] + expression[i + 1]):
                output.append(stack.pop())
            stack.push(expression[i] + expression[i + 1])
            flag = True
        elif is_operator(expression[i]):
            while not stack.is_empty() and get_priority(stack.peek()) >= get_priority(expression[i]):
                output.append(stack.pop())
            stack.push(expression[i])

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


"""infix_expression = "3 + 14"
print(infix_expression)
print(infix_to_rpn(infix_expression))
"""
# print(infix_to_rpn("2 ** 3 ** 2"))


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
    assert infix_to_rpn("2 ** 3 ** 2") == "2 3 2 ** **"

    print("All tests passed successfully!")


test_infix_to_rpn()
