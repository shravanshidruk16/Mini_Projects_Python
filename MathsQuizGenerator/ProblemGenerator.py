import random

def generate_problem(MIN_OPERAND, MAX_OPERAND, OPERATOR):
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    while operator == "/" and right == 0:
        right = random.randint(MIN_OPERAND, MAX_OPERAND)

    exp = str(left) + " " + operator + " " + str(right)
    if operator == "/":
        answer = round(eval(exp), 2)
        return exp, answer
    else:
        answer = eval(exp)
        return exp, answer
