############################################################
# FILE : hangman.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex4 2018-2019
# DESCRIPTION : Contains hangman game
#############################################################

from hangman_helper import *


def update_word_pattern(word, pattern, letter):
    """
    Exposes all index with letter in word to
    the letter in pattern, and the remaining
    indexes will have '_' if they are not exposed
    yet, and the letter if they are exposed.

    for example 'apple' with pattern '___l_'
    and the letter 'p' will return '_ppl_'
    :param word: the exposed word
    :param pattern: the pattern
    :param letter: letter to exposed
    :return: exposed pattern
    """

    result = list()
    word_len = len(word)

    for i in range(0, word_len):
        #  if the current letter is to expose
        #  or it is exposed already
        if word[i] == letter or pattern[i] != '_':
            result.append(word[i])
        else:
            result.append('_')

    return ''.join(result)


def run_single_game(words_list):
    """
    runs a single hangman game, with random word
    from words_list. at every iteration, checks
    if the end of the game has come, and else
    recieves new letter from input.
    :param words_list:
    :return:
    """
    word = get_random_word(words_list)
    pattern = '_' * len(word)
    bad_guesses = list()
    error_count = 0
    user_msg = DEFAULT_MSG
    finished = False

    while True:
        #  check for win
        if pattern == word:
            user_msg = WIN_MSG
            finished = True

        #  check for lose
        if error_count >= MAX_ERRORS:
            user_msg = LOSS_MSG + word
            finished = True

        display_state(pattern, error_count, bad_guesses, user_msg, finished)
        if finished:
            return

        inpt = get_input()
        letter = inpt[1]

        #  check if letter is hint request
        if inpt[0] == HINT:
            filtered = filter_words_list(words_list, pattern, bad_guesses)
            user_msg = HINT_MSG + choose_letter(filtered, pattern)
            continue

        #  check if letter is valid, if not update
        #  message to error
        if letter is None or len(letter) != 1 or not letter.islower():
            user_msg = NON_VALID_MSG
            continue

        #  check if the letter is already chosen
        if pattern.find(letter) != -1 or letter in bad_guesses:
            user_msg = ALREADY_CHOSEN_MSG + letter
            continue

        #  check if it is a bad guess
        if word.find(letter) == -1:
            user_msg = DEFAULT_MSG
            bad_guesses.append(letter)
            error_count += 1
            continue

        pattern = update_word_pattern(word, pattern, letter)
        user_msg = DEFAULT_MSG


def applies_to_pattern(word, pattern):
    """
    returns True if word applies to pattern.
    e.g. if pattern is ___l_ and the word is
    apple then it applies
    :param word: the exposed word
    :param pattern: the guessed pattern
    :return: if word applies to pattern
    """

    pattern_len = len(pattern)

    if pattern_len != len(word):
        return False

    exposed = list()

    #  Filter words that the
    #  exposed letters are different
    for i in range(0, pattern_len):
        if pattern[i] == '_':
            continue

        exposed.append(pattern[i])

        if pattern[i] != word[i]:
            return False

    #  Filter words that have exposed letters
    #  in different indexes than the patter
    for i in range(0, pattern_len):
        if pattern[i] != '_':
            continue

        if word[i] in exposed:
            return False

    return True


def filter_words_list(words, pattern, wrong_guess_list):
    """
    Filters from the words list the words that apply
    to pattern, and that does not contain letters
    from wrong guesses list.
    :param words: list of words
    :param pattern: the exposed pattern
    :param wrong_guess_list: list of wrong letters
    :return: filtered list
    """

    result = list()

    wrong_guess_set = set(wrong_guess_list)

    for word in words:
        #  check if word applies to the filters
        #  required. if yes, add it to result.
        word_set = set(word)

        if len(wrong_guess_set.intersection(word_set)) > 0:
            continue

        if not applies_to_pattern(word, pattern):
            continue

        result.append(word)

    return result


def choose_letter(words, pattern):
    """
    Returns the letter that is not exposed
    in pattern and that appears the most
    in all words.
    :param words: list of words
    :param pattern: exposed pattern
    :return: the most frequent letter
    """
    #  Counter will have each letter
    #  with her count of occurrences
    counter = dict()

    for word in words:
        for i in word:
            #  Don't count letters that
            #  are already exposed
            if pattern.find(i) != -1:
                continue

            #  if counter has the letter,
            #  increase the count. else,
            #  reset the letter.
            value = counter.get(i)
            if value is not None:
                counter[i] += 1
            else:
                counter[i] = 1

    #  Search for the maximum
    maxi = (None, 0)

    for letter, value in counter.items():
        if value > maxi[1]:
            maxi = (letter, value)

    return maxi[0]


def main():
    """
    Starts a single game and then continues
    starting new games as long as the user requests
    :return:
    """
    play_again = True
    words = load_words("words.txt")

    while play_again:
        run_single_game(words)

        play_again = False
        inpt = get_input()
        if inpt[0] == PLAY_AGAIN:
            play_again = inpt[1]


if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()
