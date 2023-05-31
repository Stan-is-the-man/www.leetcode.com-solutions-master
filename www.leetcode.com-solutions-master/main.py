from collections import deque


def clear_expression(the_expression):
    for sym in the_expression:
        if sym.isspace():
            the_expression = the_expression.replace(" ", "")
    return the_expression


def multiply(x, z):
    return x * z


def division(param, param1):
    return param / param1


expression = input('Please enter an expression\n')
clear_expression(expression)

result = 0
digits = deque()
symbols = deque()

for char in expression:
    if char.isdigit():
        digits.append(float(char))
    else:
        symbols.append(char)

while symbols:
    for symbol in symbols:
        if symbol == "*":
            res = multiply(digits[0], digits[1])
            result += res
            digits.popleft()
            digits.popleft()
        elif symbol == "/":
            res = division(digits[0], digits[1])
            result += res
            symbols.popleft()
        else:
            digits.append(digits.popleft())
            symbols.append(symbols.popleft())

print(result)
