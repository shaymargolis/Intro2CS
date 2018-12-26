############################################################
# FILE : check_wordsearch.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex5 2018-2019
# DESCRIPTION : Tests for wordsearch
#############################################################


def find_word_in_matrix_right(word, matrix, dims):
    """
    Find the number of occurences of all the words in word list,
    according to direction "RIGHT" in a NONE EMPTY MATRIX
    :param word: a string representing a word
    :param matrix: matrix of n x m
    :params dims: Dimension of the matrix in RIGHT direction
    :return: Array with pairs of word and number of occurrences
    """

    #  Check if matrix is empty
    num_rows = dims[0]
    num_cols = dims[1]
    word_len = len(word)
    count_found = 0

    for i in range(0, num_rows):
        for j in range(0, num_cols):
            #  If the remaining of the row is less
            #  Than the word_len, we have no point
            #  In checking
            if word_len > num_cols-j:
                continue

            #  Check if we found sequence of word
            word_found = True
            for k in range(0, word_len):
                if matrix[i][j+k] != word[k]:
                    word_found = False
                    break

            #  If we found a sequence of word, add
            #  to the count
            if word_found:
                count_found += 1

    return count_found


def test_find_word_in_matrix_right():
    # -------------------- #
    #     First test       #
    # -------------------- #
    matrix = \
        [['g', 'o', 'g', 'o', 'g', 'o']]

    if 2 == find_word_in_matrix_right('gogo', matrix, [1, 6]):
        print("First test success")
    else:
        print("First test failure")

    # -------------------- #
    #     Second test      #
    # -------------------- #
    matrix = \
        [['g', 'o', None, 'o', 'g', 'o']]

    if 1 == find_word_in_matrix_right('ogo', matrix, [1, 6]):
        print("Second test success")
    else:
        print("Second test failure")

    # -------------------- #
    #     Third test       #
    # -------------------- #
    matrix = \
        [['g', 'o'],
         ['g', 'o']]

    if 2 == find_word_in_matrix_right('go', matrix, [2, 2]):
        print("Third test success")
    else:
        print("Third test failure")

    # -------------------- #
    #     Fourth test      #
    # -------------------- #
    matrix = \
        [['g', 'o'],
         ['g', 'o']]

    if 0 == find_word_in_matrix_right('go', matrix, [0, 0]):
        print("Fourth test success")
    else:
        print("Fourth test failure")

    # -------------------- #
    #      Fifth test      #
    # -------------------- #
    matrix = \
        [['a', 'g', 'o'],
         ['b', 'b']]

    if 0 == find_word_in_matrix_right('go', matrix, [2, 2]):
        print("Fifth test success")
    else:
        print("Fifth test failure")

    pass


if __name__ == "__main__":
    test_find_word_in_matrix_right()
