############################################################
# FILE : ex7.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex7 2018-2019
# DESCRIPTION : Recursion methods
#############################################################


def print_to_n(n):
    """
    Prints the integers from 1 to n
    :param n: integer
    :return: nothing
    """
    #  Don't print anything if
    #  n is lower than 1
    if n < 1:
        return

    #  First print the n-1 items
    #  lower, then n
    print_to_n(n-1)
    print(n)


def print_reversed(n):
    """
    Prints the integers from n to 1
    :param n: integer
    :return: nothing
    """
    #  Don't print anything if
    #  n is lower than 1
    if n < 1:
        return

    #  First print n, then the n-1
    #  items lower than it
    print(n)
    print_reversed(n-1)


def is_prime(n):
    """
    Returns true if n is a prime
    integer.
    :param n:
    :return: Bool if n is prime
    """

    #  The lecturer decided that
    #  1 is not a prime number :(
    if n < 2:
        return False

    return not has_divisor_smaller_than(n, n-1)


def has_divisor_smaller_than(n, i):
    """
    Returns true if n has a divisor smaller
    than i.
    :param n: integer
    :param i: integer
    """

    #  1 divides every number so no
    if i <= 1:
        return False

    #  Check if n divides by i
    if n % i == 0:
        return True

    return has_divisor_smaller_than(n, i-1)


def factorial(n):
    """
    Calculates factorial of n
    :param n: Integer
    :return:
    """

    if n <= 1:
        return 1

    return n * factorial(n-1)


def exp_n_x(n, x):
    """
    Returns the sum from 1 to n of
    taylor series of exp(x)
    :param n: integer
    :param x: real number
    :return: taylor series of exp(x)
    from 1 to n
    """

    if n == 0:
        return 1

    return x**n/factorial(n) + exp_n_x(n-1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    Moves n hanoi plates from src to dest
    :param hanoi: hanoi object
    :param n: number of plates
    :param src: source
    :param dest: destination
    :param temp: leftover
    :return:
    """

    if n == 0:
        return

    #  Moves top n-1 plates from src to temp
    play_hanoi(hanoi, n-1, src, temp, dest)
    #  Moves last one to dest
    hanoi.move(src, dest)
    #  Moves n-1 top from temp to dest
    play_hanoi(hanoi, n-1, temp, dest, src)


def possible_sequences(char_list, n):
    """
    Returns list of all possible sequences of letters
    from char_list with with len of n
    :param char_list: array of letters
    :param n: length of sequence
    :return:
    """

    if n == 0:
        return []

    if n == 1:
        return char_list

    result = []

    #  For every letter, concate it with all possible strings
    #  of length n-1 with same letters (since we allow repeats)
    for letter in char_list:
        for n_minus_1 in possible_sequences(char_list, n-1):
            result.append(letter + n_minus_1)

    return result


def print_sequences(char_list, n):
    """
    Prints all possible sequences of letters
    from char_list in length of n
    :param char_list: array of letters
    :param n: length of sequence
    :return:
    """

    for word in possible_sequences(char_list, n):
        print(word)


def possible_no_repetition_sequences(char_list, n):
    """
    Returns list of all possible sequences of letters
    when no letter is repeated. from char_list
    len of n.
    :param char_list: array of letters
    :param n: length of sequence
    :return:
    """

    if n == 0:
        return []

    #  If the length of the possible
    #  strings is 1 just return all
    #  the letters
    if n == 1:
        return char_list

    result = []

    #  For every letter, concat it with all the possible
    #  arrangements of it with the rest of the letters
    #  (since we do not allow repeats) with length of n-1
    for letter in char_list:
        char_list_w_letter = char_list.copy()
        char_list_w_letter.remove(letter)

        possible_seq = possible_no_repetition_sequences(char_list_w_letter, n-1)

        for n_minus_1 in possible_seq:
            result.append(letter + n_minus_1)

    return result


def print_no_repetition_sequences(char_list, n):
    """
    Prints all possible sequences of letters
    when we are not repeating any letter
    from char_list in length of n
    :param char_list: array of letters
    :param n: length of sequence
    :return:
    """

    for word in possible_no_repetition_sequences(char_list, n):
        print(word)


def parentheses_less_depth(n, deep):
    """
    Returns the strings with N partheses
    that their depth is less deeper than deep
    (depth is the largest number of parentheses
    inside one another, for example the depth
    of the string "(())()" is 2)
    :param n: length of string
    :param deep: maximum depth of generated
    strings.
    :return:
    """

    #  We can't generate an 0-deep
    if deep == 0 or n == 0:
        return []

    if deep == 1:
        return ["()" * n]

    #  The options for deep-depth, are these:
    #  ( n-2, deep-1), string1 (less than deep-depth) + deep-depth string
    #  deep-depth string + string2 (less than deep-depth)

    result = list()

    #  Append all strings with format (n-1, deep-1)
    less_than = parentheses_less_depth(n-1, deep-2)
    for string in parentheses_less_depth(n-1, deep-1):
        if string in less_than:
            continue

        result.append("(" + string + ")")

    #  Append all strings with format
    #  string1 (less than deep-depth) + deep-depth string
    #  deep-depth string + string2 (less than deep-depth)
    for i in range(1, n):
        less_than = parentheses_less_depth(n-i, deep-1)
        for string1 in parentheses_less_depth(n-i, deep):
            if string1 in less_than:
                continue

            for string2 in parentheses_less_depth(i, deep):
                #  Check if generated strings are not already in result,
                #  if no add them.
                if string1+string2 not in result:
                    result.append(string1+string2)

                if string2+string1 not in result:
                    result.append(string2+string1)

    return result + parentheses_less_depth(n, deep-1)


def parentheses(n):
    """
    Returns list of all the strings with valid number
    of n parentheses.
    :param n:
    :return:
    """

    return parentheses_less_depth(n, n)


def up_and_right_from(n, k, x, y):
    """
    Prints all routes from (x, y) to (n,k)
    using only up and right methods.
    :param n: int
    :param k: int
    :return:
    """

    if (n, k) == (x, y):
        return []

    if (n, k) == (x+1, y):
        return ['r']

    if (n, k) == (x, y+1):
        return ['u']

    top = [x, y+1]
    right = [x+1, y]

    result = []

    #  As long as top is inside the matrix
    #  and is not beyond the k (target y)
    if top[1] <= k:
        for route in up_and_right_from(n, k, top[0], top[1]):
            result.append('u' + route)

    #  As long as right is inside the matrix
    #  and is not beyond the n (target x)
    if right[0] <= n:
        for route in up_and_right_from(n, k, right[0], right[1]):
            result.append('r' + route)

    return result


def up_and_right(n, k):
    """
    Prints all routes from (0,0) to (n,k)
    using only up and right methods.
    :param n: int
    :param k: int
    :return:
    """

    routes = up_and_right_from(n, k, 0, 0)

    #  There are no routes, or (n,k)=(0,0)
    if routes is []:
        return

    for route in routes:
        print(route)


def flood_fill(image, start):
    """
    Fills the empty cells near start point
    with water.
    :param image: Matrix of points
    :param start: Start point of flood
    :return: Nothing
    """

    cols = len(image[0])
    rows = len(image)

    #  Fill image cell with 't' = temp
    #  to avoid filling same cell twice
    image[start[0]][start[1]] = 't'

    #  Find cell neighbors
    right = [start[0], start[1]+1]
    bottom = [start[0]+1, start[1]]
    left = [start[0], start[1]-1]
    top = [start[0]-1, start[1]]

    if right[0] < cols and image[right[0]][right[0]] == '.':
        flood_fill(image, right)

    if left[0] > 0 and image[left[0]][left[1]] == '.':
        flood_fill(image, left)

    if bottom[1] < rows and image[bottom[0]][bottom[1]] == '.':
        flood_fill(image, bottom)

    if top[1] > 0 and image[top[0]][top[1]] == '.':
        flood_fill(image, top)

    image[start[0]][start[1]] = '*'

