############################################################
# FILE : wordsearch.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex5 2018-2019
# DESCRIPTION : Search for words in matrix
#############################################################

import sys
import os.path

ARGS_NUM = 5
WORD_FILE_INDEX = 1
MATRIX_FILE_INDEX = 2
OUTPUT_FILE_INDEX = 3
DIRECTIONS_INDEX = 4

VALID_DIRECTIONS = ['u', 'r', 'd', 'l', 'w', 'x', 'y', 'z']

MATRIX_SEPARATOR = ","


def direction_valid(direction):
    """
    Returns true if direction is valid,
    false if not and error message.
    :param direction: A letter of direction
    :return: True or False
    """

    if direction not in VALID_DIRECTIONS:
        return direction + " is not a valid direction."

    return None


def check_input_args(args):
    """
    Checks if input arguments are valid,
    if yes returns None, if Returns
    the error message
    :param args: The start arguments
    :return: None on success, error string
        on failure
    """

    #  Make sure that the number of args
    #  is valid
    if len(args) != ARGS_NUM:
        return "The number of args must be " + str(ARGS_NUM)

    word_file = args[WORD_FILE_INDEX]
    matrix_file = args[MATRIX_FILE_INDEX]
    output_file = args[OUTPUT_FILE_INDEX]
    directions = args[DIRECTIONS_INDEX]

    #  Return error if word_file or matrix_file
    #  do not exist
    if not os.path.isfile(word_file):
        return "The word file does not exists."

    if not os.path.isfile(matrix_file):
        return "The matrix file does not exists."

    #  For every letter in directions,
    #  Check if it is valid
    for direction in set(directions):
        result = direction_valid(direction)
        if result is not None:
            return result

    return None


def read_file_lines(filename):
    """
    Returns array of all the lines in filename
    :param filename: path to file
    :return: array of all lines
    """

    f = open(filename, 'r')
    lines = [i[:-1] for i in f.readlines()]
    f.close()

    arr[:-1]

    return lines


def read_wordlist_file(filename):
    """
    Returns array of all the lines in filename,
    matching the words in the words file
    :param filename: path to word file
    :return: array of all the words in word file
    """

    return read_file_lines(filename)


def read_matrix_file(filename):
    """
    Returns matrix of all the letters in filename,
    matching the pattern in the question
    :param filename:
    :return:
    """

    matrix = []

    #  Read all lines, and separate to letters
    #  by the separator MATRIX_SEPARATOR
    lines = read_file_lines(filename)
    for line in lines:
        matrix.append(line.split(MATRIX_SEPARATOR))

    return matrix


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


def transform_matrix(matrix, new_pos, dims):
    """
    Returns new matrix from matrix with the new
    position rule (i,j) -> new_pos(i,j)
    :param matrix: The old matrix
    :param new_pos: new position functoins
    :param dims: Dimensions of te new matrix
    :return: The transformed matrix
    """
    new_matrix = list()

    #  Create rows
    for i in range(0, dims[0]):
        #  Create cols
        line = []
        for j in range(0, dims[1]):
            line.append(new_pos(matrix, i, j))

        new_matrix.append(line)

    return new_matrix


def u_right_pos(matrix, i, j):
    """
    Returns the element in the pos <i,j>
    in the matrix that is read from left to right
    As if the matrix was read from bottom to up
    :param matrix: Original matrix
    :param i: row
    :param j: col
    :return: val in pos or None if not matches
    any place in the original matrix
    """

    rows = len(matrix)
    return matrix[rows-j-1][i]


def l_right_pos(matrix, i, j):
    """
    Returns the element in the pos <i,j>
    in the matrix that is read from left to right
    As if the matrix was read from right to left
    :param matrix: Original matrix
    :param i: row
    :param j: col
    :return: val in pos or None if not matches
    any place in the original matrix
    """

    cols = len(matrix[0])
    return matrix[i][cols-j-1]


def w_right_pos(matrix, i, j):
    """
    Returns the element in the pos <i,j>
    in the matrix that is read from left to right
    As if the matrix was read as diagonals
    (right top diagonal)
    :param matrix: Original matrix
    :param i: row
    :param j: col
    :return: val in pos or None if not matches
    any place in the original matrix
    """

    #  i is the number of the diag
    #  (first diag is 0,0 -> 0,0)
    #  j is the progress inside the diag.
    rows = len(matrix)
    cols = len(matrix[0])

    start_i = i
    start_j = 0

    if i >= rows:
        start_i = rows-1
        start_j = i-rows+1

    #  Progress inside the diag
    start_i -= j
    start_j += j

    if start_i not in range(0, rows) \
        or start_j not in range(0, cols):
        return None

    return matrix[start_i][start_j]


def y_right_pos(matrix, i, j):
    """
    Returns the element in the pos <i,j>
    in the matrix that is read from left to right
    As if the matrix was read as diagonals
    (right bottom diagonal)
    :param matrix: Original matrix
    :param i: row
    :param j: col
    :return: val in pos or None if not matches
    any place in the original matrix
    """

    #  i is the number of the diag
    #  (first diag is 0,0 -> 0,0)
    #  j is the progress inside the diag.
    rows = len(matrix)
    cols = len(matrix[0])

    start_i = 0
    start_j = cols-i-1

    if i >= cols:
        start_i = i-cols+1
        start_j = 0

    #  Progress inside the diag
    start_i += j
    start_j += j

    if start_i not in range(0, rows) \
        or start_j not in range(0, cols):
        return None

    return matrix[start_i][start_j]


def get_dims(matrix):
    """
    Returns the dimensions of a matrix
    :param matrix:
    :return:
    """
    rows = len(matrix)
    if rows == 0:
        return [0, 0]

    cols = len(matrix[0])
    return [rows, cols]


def print_matrix(matrix, dims):
    """
    Prints matrix with specific dimensions
    :return: nothing
    """
    dims = get_dims(matrix)

    for i in range(0, dims[0]):
        line = ""
        for j in range(0, dims[1]):
            let = matrix[i][j]
            if let is None:
                line += " " + ","
            else:
                line += let + ","

        print(line)


def get_right_matrix(matrix, direction):
    """
    Returns right direction matrix that is equivilent
    to the given direction.
    :param matrix: A matrix
    :param direction: A direction in VALID_DIRECTIONS
    :return: Right equivilent matrix
    """
    dims = get_dims(matrix)
    rows = dims[0]
    cols = dims[1]

    #  If the direction is not RIGHT, transform
    #  the matrix to a RIGHT direction equal one.
    #  Diagonal matrices will have None as letter
    #  Outside of the diagonal.
    if direction == 'u':
        matrix = transform_matrix(matrix, u_right_pos, [cols, rows])

    #  Down direction is like transforming to up and then left
    if direction == 'd':
        matrix = transform_matrix(matrix, u_right_pos, [cols, rows])
        matrix = transform_matrix(matrix, l_right_pos, [cols, rows])

    if direction == 'l':
        matrix = transform_matrix(matrix, l_right_pos, [rows, cols])

    if direction == 'w':
        matrix = transform_matrix(matrix, w_right_pos, [rows+cols-1, cols])

    #  Z direction is like transforming to W and then L
    if direction == 'z':
        matrix = transform_matrix(matrix, w_right_pos, [rows+cols-1, cols])
        matrix = transform_matrix(matrix, l_right_pos, [rows+cols-1, cols])

    if direction == 'x':
        matrix = transform_matrix(matrix, y_right_pos, [rows+cols-1, cols])
        matrix = transform_matrix(matrix, l_right_pos, [rows+cols-1, cols])

    #  Y direction is like transforming to X and then L
    if direction == 'y':
        matrix = transform_matrix(matrix, y_right_pos, [rows+cols-1, cols])

    return matrix


def find_words_in_matrix(word_list, matrix, directions):
    """
    Find the number of occurences of all the words in word list,
    according to directions (in VALID_DIRECTIONS)
    :param word_list: list of words
    :param matrix: matrix of n x m letters
    :param directions: letters representing directions
    :return: Array with pairs of word and number of occurrences
    """

    result = dict()

    #  For every direction, get the count of every word appearence
    for direction in set(directions):
        #  Get right equivilent matrix to matrix
        r_matrix = get_right_matrix(matrix, direction)
        dims = get_dims(r_matrix)

        for word in word_list:
            count = find_word_in_matrix_right(word, r_matrix, dims)

            #  Add result to dict if it is bigger than 0
            if count == 0:
                continue

            if word in result:
                result[word] += count
            else:
                result[word] = count

    #  Create result array
    result_arr = list()

    for word, count in result.items():
        result_arr.append((word, count))

    return result_arr


def write_output_file(results, output_filename):
    """
    Write results dictionary to output_filename
    :return:
    """

    lines = ""

    for x, y in results:
        lines += x + "," + str(y) + "\n"

    f = open(output_filename, 'w')
    if f:
        f.write(lines)

    f.close()
    return


def main():
    """
    Starts the program from system args.
    usage: wordsearch.py word_file matrix_file output_file directions

    First reads word and matrix files, and then calls the find_word_in_matrix
    function, at the end writes the result to the output file.
    """
    args = sys.argv

    #  Validate input arguments
    check_input = check_input_args(args)
    if check_input is not None:
        print(check_input)
        return 1

    #  Load word & matrix files, and directions
    word_file = read_wordlist_file(args[WORD_FILE_INDEX])
    matrix = read_matrix_file(args[MATRIX_FILE_INDEX])

    directions = args[DIRECTIONS_INDEX]

    #  Get result and write it
    result = find_words_in_matrix(word_file, matrix, directions)
    write_output_file(result, args[OUTPUT_FILE_INDEX])

    return 0


if __name__ == "__main__":
    main()
