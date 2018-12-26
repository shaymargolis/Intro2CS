#############################################################
# FILE : calculate_mathematical_expression.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex2 2018-2019
# DESCRIPTION : Set of functions used to calculate
#               Mathematical expressions
#############################################################


def calculate_mathematical_expression(i1, i2, operation):
    """
        calculates i1 (op) i2, according to the operation.
        for example, for i1=3, i2=2, operation = "*", the
        result will be 3*2 = 6

        allowed operations: /, *, -, +
    """

    #  If the operation is 'divide by', require that i2 will
    #  not be zero, to prevent dividing by zero.
    if operation == '/':
        if i2 == 0:
            return None

        return i1/i2

    if operation == '*':
        return i1*i2

    if operation == '-':
        return i1-i2

    if operation == '+':
        return i1+i2

    return None


def calculate_from_string(string):
    """
        recieves a string with mathematical expression,
        as "1 + 5" and returns the answer as float.
        the format must be "(num1) (operation) (num2)"
    """

    #  splits the string to the numbers and operations using split()
    #  and then verifies that the format is correct
    #  (3 elements in the parameters array)
    parameters = string.split()
    if len(parameters) != 3:
        return None

    return calculate_mathematical_expression(float(parameters[0]),
                                             float(parameters[2]),
                                             parameters[1])
