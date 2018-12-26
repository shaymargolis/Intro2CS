#############################################################
# FILE : check_maximum.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex3 2018-2019
# DESCRIPTION : Contains function to test maximum
#############################################################

from ex3 import maximum


def test_maximum_case(num_test, array, expected):
    """
    Checks if maximum(array) equals expected,
    and prints message accordingly.
    :param num_test:
    :param array:
    :param expected:
    :return:
    """
    if maximum(array) == expected:
        print("Test", num_test, "OK")
        return

    print("Test", num_test, "FAIL")


def test_maximum():
    """
    tests maximum function
    with different cases
    :return:
    """
    test_maximum_case(0, [0, 0, 0], 0)
    test_maximum_case(1, [2, 0, 0], 2)
    test_maximum_case(2, [1, 2, 1], 2)
    test_maximum_case(3, [4, 5, 6], 6)
    test_maximum_case(4, [4.5, 5.1, 6.7], 6.7)
    test_maximum_case(5, [], None)


if __name__ == "__main__":
    test_maximum()
