############################################################
# FILE : ex8.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex8 2018-2019
# DESCRIPTION : Backtracking methods and diffrent approach
#############################################################

import math


def is_legal_fill(board, row, col, num):
    """
    Checks if we can position num inside board[i][j]
    (if we don't have 2 same numbers in row, col or box).
    :param board: Soduko NxN board
    :param row: row
    :param col: col
    :param num: number to position
    :return: Boolean
    """

    N = len(board)
    N_sqrt = int(math.sqrt(N))
    numbers = {i for i in range(1, N+1)}

    #  Check row
    possible = numbers.copy()
    for j in range(0, N):
        #  If board[i][j] is not determined yet,
        #  it is okay.
        if board[row][j] == 0:
            continue

        #  We already scanned this number in this
        #  row or it is an invalid character to be
        #  in a soduko board.
        if board[row][j] not in possible:
            return False

        possible.remove(board[row][j])

    #  Check col
    possible = numbers.copy()
    for i in range(0, N):
        #  If board[i][j] is not determined yet,
        #  it is okay.
        if board[i][col] == 0:
            continue

        #  We already scanned this number in this
        #  row or it is an invalid character to be
        #  in a soduko board.
        if board[i][col] not in possible:
            return False

        possible.remove(board[i][col])

    #  Check box
    #  Find startX and startY of box
    i = (row // N_sqrt) * N_sqrt
    j = (col // N_sqrt) * N_sqrt
    cur = (i, j)
    possible = numbers.copy()

    while cur is not None:
        cur_i = cur[0]
        cur_j = cur[1]
        #  If board[i][j] is not determined yet,
        #  it is okay.
        if board[cur_i][cur_j] == 0:
            cur = next_index(N_sqrt, cur_i, cur_j)
            continue

        #  We already scanned this number in this
        #  row or it is an invalid character to be
        #  in a soduko board.
        if board[cur_i][cur_j] not in possible:
            return False

        possible.remove(board[cur_i][cur_j])

        #  next position inside the box
        cur = next_index(N_sqrt, cur_i, cur_j)

    return True


def is_solved(board):
    """
    Checks if a soduko board is solved
    (has no zeros)
    :param board: A soduko NxN board.
    :return: True or False
    """

    N = len(board)
    numbers = {i for i in range(1, N+1)}

    for i in range(1, N):
        for j in range(1, N):
            #  If we have in the final solution
            #  something that is not a valid numbre
            #  then it is not a valid solution
            if board[i][j] not in numbers:
                return False

    return True


def next_index(n, i, j):
    """
    returns the next index when scanning board from
    left to right and top to bottom.
    Assumes board has at least one row
    :param board:  A NxN soduko board
    :param i:  The row to start with
    :param j:  The column to start with
    :return: next box location in tuple, or None
    if we reached end of board
    """

    #  If we can go to the right
    if j < n-1:
        return i, j+1

    #  If we reached end of row,
    #  go to next row
    if j == n-1 and i < n-1:
        return i+1, 0

    #  If not, we reached end of matrix.
    return None


def solve_soduko_position(board, i, j):
    """
    Solves a soduko board by backtracking,
    if the succeseeds it returns the solved
    board, else it will return the original
    borad.
    It assumes that the board is full until the i,j
    box.
    :param board: A NxN soduko board
    :param i: The row to start with
    :param j: The column to start with
    :return: solved board or original board
    on failure.
    """

    N = len(board)

    #  If the number here is already set,
    #  continue to next box
    if board[i][j] != 0:
        next = next_index(N, i, j)
        if next is None:
            return is_legal_fill(board, i, j, board[i][j])

        return solve_soduko_position(board, next[0], next[1])

    #  Try putting inside board[i][j] all options
    #  from 1 to n, that is not tried in the box/row
    #  /column of the position yet.
    next = next_index(N, i, j)
    for num in range(1, N+1):
        board[i][j] = num

        if not is_legal_fill(board, i, j, num):
            continue

        if next is not None:
            solve_soduko_position(board, next[0], next[1])

        if is_solved(board):
            return True

    #  Reset this position
    board[i][j] = 0
    return False


def solve_sudoku(board):
    """
    Solves a soduko board by backtracking,
    if the succeseeds it returns the solved
    board, else it will return the original
    borad.
    :param board: A NxN soduko board
    :return: true on success or false on failure.
    """

    if len(board) == 0 or len(board[0]) == 0:
        return True

    return solve_soduko_position(board, 0, 0)


def print_k_subsets_without(n, cur, k):
    """
    Prints all subsets of {0,...,n-1}
    with k elements
    :param n: number of total numbers
    :param k: length of subset
    :return: list of all subsets
    """

    if len(cur) == k:
        print(cur)

    if n == 0:
        return

    #  The possebilities to continue the
    #  cur array to get a k-subset of 0,..,n-1
    #  in increasing order, are all numbers
    #  that are bigger than the maximum in cur
    nums = [i for i in range(0, n)]
    if len(cur) != 0:
        nums = list(filter(lambda x: x > max(cur), nums))

    #  Add every number to next and print it
    for num in nums:
        next = cur.copy()
        next += [num]

        print_k_subsets_without(n, next, k)


def print_k_subsets(n, k):
    """
    Prints all subsets of {0,...,n-1}
    with k elements
    :param n: number of total numbers
    :param k: length of subset
    :return: list of all subsets
    """

    print_k_subsets_without(n, [], k)


def fill_k_subsets_without(n, cur, k, lst):
    """
    Prints all subsets of {0,...,n-1}
    with k elements, when the current made
    string is cur.
    :param n: number of total numbers
    :param k: length of subset
    :return: list of all subsets
    """

    if len(cur) == k:
        lst.append(cur)

    if n == 0:
        return

    #  The possebilities to continue the
    #  cur array to get a k-subset of 0,..,n-1
    #  in increasing order, are all numbers
    #  that are bigger than the maximum in cur
    nums = [i for i in range(0, n)]
    if len(cur) != 0:
        nums = list(filter(lambda x: x > max(cur), nums))

    #  Add every number to next and print it
    for num in nums:
        next = cur.copy()
        next += [num]

        fill_k_subsets_without(n, next, k, lst)


def fill_k_subsets(n, k, lst):
    """
    Prints all subsets of {0,...,n-1}
    with k elements
    :param n: number of total numbers
    :param k: length of subset
    :return: list of all subsets
    """

    fill_k_subsets_without(n, [], k, lst)


def return_k_subsets(n, k):
    """
    Returns all subsets of {0,...,n-1}
    with k elements
    :param n: number of total numbers
    :param k: length of subset
    :return: list of all subsets
    """

    nums = [i for i in range(0, n)]
    result = []

    if k == 0:
        return [[]]

    if n == 0:
        return []

    #  Subsets with lenght of 1 are just
    #  the numbers
    if k == 1:
        return [[i] for i in range(0, n)]

    #  For every number between 0, ..., n-1,
    #  concate to it all the subsets with the
    #  len of k-1, where the items are larger
    #  then the num (increasing order)
    for num in nums:
        reminder = return_k_subsets(n, k-1)
        reminder = list(filter(lambda x: min(x) > num, reminder))

        for rem in reminder:
            rem = [num] + rem
            result.append(rem)

    return result
