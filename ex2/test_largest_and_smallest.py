#############################################################
# FILE : test_largest_and_smallest.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex2 2018-2019
# DESCRIPTION : Tests largest and smallest function
#############################################################

import largest_and_smallest as ls


def test_input(input, expected_max, expected_min):
    """
        Tests single input, and returns true if the output
        equals the expected output.
    """

    (result_max, result_min) = ls.largest_and_smallest(input[0], input[1], input[2])

    if result_max == expected_max and result_min == expected_min:
        return True

    return False


def test_largest_and_smallest():
    """
        Tests largest_and_smallest function for
        five different data sets.
        :return: True on success, False on failure
    """
    test_success = True

    #  First input
    test_success &= test_input([1, 2, 3], 3, 1)

    #  Second input
    test_success &= test_input([2, 3, 1], 3, 1)

    #  Third input
    test_success &= test_input([1, 3, 2], 3, 1)

    #  Forth input
    test_success &= test_input([3, 1, 2], 3, 1)

    #  Fifth input
    test_success &= test_input([-1, -2, -3], -1, -3)

    return test_success

if __name__ == "__main__":
    result = test_largest_and_smallest()

    if result == True:
        print("Function 4 test success")
    else:
        print("Function 4 test fail")
