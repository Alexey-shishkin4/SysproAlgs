from structures import Stack


priorities = {
        '(': 0,
        ')': 0,
        '!': 1,
        '~': 1,
        '**': 2,
        '*': 4,
        '/': 4,
        '%': 4,
        '+': 3,
        '-': 3,
        '>>': 5,
        '<<': 6,
        '<': 7,
        '<=': 7,
        '>': 7,
        '>=': 7,
        '==': 8,
        '!=': 8,
        '&': 9,
        '^': 10,
        '|': 11,
        '&&': 12,
        '||': 13
    }


def get_priority(op):
    if op in priorities:
        return priorities[op]


def is_operator(token):
    operators = \
        ['!', '~', '**', '+', '-', '*', '/', '%', '>>', '<<', '<', '<=', '>=', '==', '!=', '&', '^', '|', '&&', '||']
    return token in operators


def infix_to_rpn(expression):
    tokens = []
    d = 0
    n = len(expression)
    flag = False
    for i in range(n):
        if flag:
            flag = False
            continue
        if expression[i] == ' ':
            if d != 0:
                tokens.append(str(d))
                d = 0
            continue
        if i + 1 < n:
            if (expression[i] + expression[i + 1]) in priorities:
                tokens.append(expression[i] + expression[i + 1])
                flag = True
                continue
        if expression[i] == ')':
            if d != 0:
                tokens.append(str(d))
                d = 0
            tokens.append(expression[i])
        elif expression[i] in priorities:
            tokens.append(expression[i])
        elif expression[i].isdigit():
            d *= 10
            d += int(expression[i])
    if d != 0:
        tokens.append(str(d))
    output = []
    stack = Stack()
    right_ops = ['!', '~', '**']
    for i in tokens:
        if i == '(':
            stack.push(i)
        elif i == ')':
            while stack.peek() != '(':
                oper = stack.pop()
                output.append(oper)
            stack.pop()
        elif i.isdigit():
            output.append(i)
        elif is_operator(i):
            if i not in right_ops:
                while not stack.is_empty() and\
                        (get_priority(i) <= get_priority(stack.peek()) or stack.peek() in right_ops):
                    output.append(stack.pop())
            stack.push(i)

    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


"""infix_expression = "!5 | (3 & 7)"
print(infix_expression)
print(infix_to_rpn(infix_expression))"""

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
