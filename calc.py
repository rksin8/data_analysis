# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.

#! last edit 9 May 2024 by Ali

def compute(expression):
    Value1, operator, Value2 = expression.split(' ')
    Value1, Value2 = float(Value1), float(Value2)
    if operator == '+':
        return Value1 + Value2
    elif operator == '-':
        return Value1 - Value2
    elif operator == '*':
        return Value1 * Value2
    elif operator == '/':
        return Value1 / Value2
    else:
        print('unknown operator!')
        return None
