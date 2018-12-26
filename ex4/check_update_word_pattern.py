############################################################
# FILE : check_update_word_pattern.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex4 2018-2019
# DESCRIPTION : Checks the function word_update_check
#############################################################

from hangman import update_word_pattern


def check_update_word_pattern():
    """
    Checks the update_word_pattern
    for 4 different inputs.
    :return:
    """

    valid = True

    if update_word_pattern('banana', 'b_____', 'n') != 'b_n_n_':
        valid = False

    if update_word_pattern('banana', '______', 'f') != '______':
        valid = False

    if update_word_pattern('', '', 'n') != '':
        valid = False

    if update_word_pattern('aaa', '___', 'a') != 'aaa':
        valid = False

    return valid


if __name__ == "__main__":
    result = check_update_word_pattern()

    if result:
        print('Function "update_word_pattern" test success')
    else:
        print('Function "update_word_pattern" test fail')
