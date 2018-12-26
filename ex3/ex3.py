#############################################################
# FILE : ex3.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex3 2018-2019
# DESCRIPTION : Contains different function in ex3
#############################################################

import math


def input_list():
    """
    Retrieves strings from input until it gets empty string
    as an input, then it returns all the strings as a list.
    :return: List of strings from input or empty set
    """
    result = []

    #  Gets initial input
    user_input = input()

    #  While user_input is not empty string
    #  (The input not terminated), add it to
    #  user_input and get another string.
    while user_input != "":
        result.append(user_input)
        user_input = input()

    return result


def concat_list(str_list):
    """
    concates list of strings to one string,
    with spaces between every string to another.
    :param str_list: list of strings to concate
    :return: a concated string
    """
    list_len = len(str_list)

    #  If the list length is 0 return empty result
    if list_len == 0:
        return ""

    result = ""
    i = 0

    #  Add all middle string with spaces after them
    while i < list_len-1:
        result += str_list[i] + " "
        i += 1

    #  Add last string without space afterwards
    result += str_list[i]

    return result


def maximum(num_list):
    """
    This function returns the maximum
    number from num_list
    :param num_list: list of numbers
    :return: the maximum number
    """

    list_len = len(num_list)

    if list_len == 0:
        return None

    max_val = 0

    #  Check every number in the list
    #  If it is larger than max_val
    #  then set it as max_val
    for i in range(0, list_len):
        if num_list[i] > max_val:
            max_val = num_list[i]

    return max_val


def cyclic(lst1, lst2):
    """
    Checks if lst1 is cyclic permutation
    of lst2
    :param lst1: list
    :param lst2: list
    :return: true if cyclic permutation
    """

    lst1_len = len(lst1)
    lst2_len = len(lst2)

    #  If both lists are empty, they are cyclic
    if lst1_len == 0 and lst2_len == 0:
        return True

    #  If the len is different they aren't cyclic
    if lst1_len != lst2_len:
        return False

    #  For on all m values and check if the cyclic
    #  permutation from lst1+m is equal to lst2
    for m in range(0, lst1_len):
        is_equal = True

        #  Checks if lst1+m is equal to lst2
        #  If not it sets is_equal to false
        for i in range(0, lst1_len):
            if lst1[i] != lst2[(i+m)%lst1_len]:
                is_equal = False

        if is_equal:
            return True

    return False


def seven_boom(n):
    """
    Returns list of the game "seven boom"
    with numbres from 1 to n, and "boom" instead
    of the numbers that contain 7 or divides by 7.
    :param n: The number of numbers to create
    :return: List of the game
    """

    result = []

    #  If i divides by 7, or contains the char
    #  7, append "boom", else, append the number.
    for i in range(1, n+1):
        i_str = str(i)
        if i % 7 == 0 or i_str.find('7') != -1:
            result.append("boom")
        else:
            result.append(i_str)

    return result


def histogram(n, num_list):
    """
    creates histogram of the numbers
    1,...,n appreaing in num_list
    :param n:
    :param num_list:
    :return:
    """

    result = []
    list_len = len(num_list)

    #  for every number 0<=i<=n, count
    #  the number of times it appears
    #  in num_list and append it to result.
    for i in range(0, n):
        count = 0
        for j in range(0, list_len):
            if num_list[j] == i:
                count += 1

        result.append(count)

    return result


def prime_factors(n):
    """
    Calculates the prime factors of n
    and returns list of them sorted from
    biggest to the smallest
    :param n: the number to calculate
    :return: the prime factors of n
    """

    result = []

    #  For every number from 2 to n,
    #  check if it divides n. if it
    #  does, it is prime because every
    #  prime number before already divided
    #  it.
    for i in range(2, n+1):
        #  divide n by i until there is leftover
        #  and add it as a factor
        while n % i == 0:
            result.append(i)
            n /= i

    return result


def cartesian(lst1, lst2):
    """
    Calculates cartesian product of
    lst1 x lst2
    :param lst1: List
    :param lst2: List
    :return: List of cartesian product
    """

    len1 = len(lst1)
    len2 = len(lst2)

    result = []

    #  For every i in lst1, and every
    #  j in lst2, append [lst1[i], lst2[j]]
    #  to the result, to produce cartesian
    #  result.
    for i in range(0, len1):
        for j in range(0, len2):
            result.append([lst1[i], lst2[j]])

    return result


def pairs(num_list, n):
    """
    Returns all the pairs of numbers from
    num_list that their sum is n
    :param num_list: list of numbers
    :param n:
    :return:
    """

    list_len = len(num_list)
    result = []

    #  For all pairs of numbers from num_list
    #  without looking at the same couple twice
    #  (different order), check if the sum is n
    #  if yes, add the pair to result
    for i in range(0, list_len):
        for j in range(i+1, list_len):
            a = num_list[i]
            b = num_list[j]

            if a + b == n:
                result.append([a, b])

    return result
