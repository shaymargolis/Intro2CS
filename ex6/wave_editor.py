############################################################
# FILE : wave_editor.py
# WRITER : shay margolis , shaymar
# EXERCISE : intro2cs1 ex6 2018-2019
# DESCRIPTION : Edit wave files
#############################################################\

import os.path
import numpy as np
import math

from wave_helper import *

CHANGE_TYPES = ['1', '2', '3', '4', '5', '6']
CHANGE_TYPE_REVERSE = '1'
CHANGE_TYPE_SPEED = '2'
CHANGE_TYPE_SLOWER = '3'
CHANGE_TYPE_HIGHER = '4'
CHANGE_TYPE_LOWER = '5'
CHANGE_TYPE_LOW_PASS = '6'

START_INDEXES = ['1', '2', '3', '4']
START_OP_CHANGE = '1'
START_OP_COMBINE = '2'
START_OP_COMPOSITE = '3'
START_OP_EXIT = '4'

SAVE_INDEXES = ['1', '2']
SAVE_OP_SAVE = '1'
SAVE_OP_CHANGE = '2'

COMPOSITE_SAMPLE_RATE = 2000
MAX_VOLUME = 32767

FREQUENCIES = {
    'A': 440,
    'B': 494,
    'C': 523,
    'D': 587,
    'E': 659,
    'F': 698,
    'G': 784,
    'Q': 0
}

INSTRUCTION_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Q']


def change_wav_reverse(audio_data):
    """
    Reverses the wav by adding the audio_data
    items in reverse order.
    :param audio_data: Wav audio data
    :return: altered audio data
    """
    result = list()

    i = len(audio_data)-1

    while i >= 0:
        result.append(audio_data[i])
        i -= 1  # Continue to next item

    return result


def change_wav_speed(audio_data):
    """
    Makes the audio_data sound faster by adding
    only the nodes with a index that is not divided
    by 2.
    :param audio_data: Wav audio data
    :return: altered audio data
    """
    result = list()
    length = len(audio_data)

    for i in range(0, length):
        if i % 2 != 0:
            continue

        result.append(audio_data[i])

    return result


def change_wav_slower(audio_data):
    """
    Makes the audio_data sound slower by adding
    an average of the left and right in the middle
    of the array
    :param audio_data: Wav audio data
    :return: altered audio data
    """
    result = list()
    length = len(audio_data)

    for i in range(0, length):
        result.append(audio_data[i])

        #  Only add a middle average in the middle of the array
        if i == length-1:
            continue

        one = np.int_(audio_data[i])
        two = np.int_(audio_data[i+1])

        result.append(list((one+two)/2))

    return result


def normalize_data(data):
    """
    Normalizes data value to be between
    32767 and -32768
    """

    if data > 32767:
        data = 32767

    if data < -32768:
        data = -32768

    return int(data)


def change_wav_higher(audio_data):
    """
    Makes the audio_data sound higher by making
    all the values higher by 1.2. If the higher
    value exceeds 32767 or -32768, it normalized
    it to the max/min.
    :param audio_data: Wav audio data
    :return: altered audio data
    """
    result = list()
    length = len(audio_data)

    for i in range(0, length):
        new_data = np.multiply(audio_data[i], 1.2)

        #  Normalize new data
        new_data[0] = normalize_data(new_data[0])
        new_data[1] = normalize_data(new_data[1])

        result.append(list(new_data))

    return result


def change_wav_lower(audio_data):
    """
    Makes the audio_data sound lower by making
    all the values lower by 1.2.
    :param audio_data: Wav audio data
    :return: altered audio data
    """
    result = list()
    length = len(audio_data)

    for i in range(0, length):
        new_data = audio_data[i]

        #  Normalize new data
        new_data[0] = int(new_data[0]/1.2)
        new_data[1] = int(new_data[1]/1.2)

        result.append(list(new_data))

    return result


def change_wav_low_pass(audio_data):
    """
    Makes low pass filter on the audio data
    by setting each node value to be the average
    of its neighbors.
    :param audio_data: Wav audio data
    :return: altered audio data
    """
    result = list()
    length = len(audio_data)

    if length == 1:
        return audio_data

    for i in range(0, length):
        #  Add the average of the neighbor nodes to the node
        #  And with special treatment to first and last nodes.
        one = np.int_(audio_data[i])

        if i == 0:
            two = np.int_(audio_data[1])

            result.append(list((one+two)/2))
            continue

        two = np.int_(audio_data[i-1])

        if i == length-1:
            result.append(list((one+two)/2))
            continue

        thr = np.int_(audio_data[i+1])
        result.append(list((one+two+thr)/3))

    result_int = map(lambda x: [int(x[0]), int(x[1])], result)

    return list(result_int)


def change_wav(sample_rate, audio_data):
    """
    Starts menu to change exising WAV data.
    Presents menu of options, and calls the
    modifying function accordingly
    :param sample_rate: Sample rate
    :param audio_data: array of WAV data
    :return: sample_rate, audio_data
    after transform
    """
    #  Get type of change
    print("Available modifications: ")
    print("    1. Reverse sound")
    print("    2. Speed sound")
    print("    3. Slow sound")
    print("    4. Higher sound")
    print("    5. Lower sound")
    print("    6. Low pass filter")

    op = input('>> ')

    if op not in CHANGE_TYPES:
        print("Not a supported type.")
        return -1

    if op == CHANGE_TYPE_REVERSE:
        result = change_wav_reverse(audio_data)

    if op == CHANGE_TYPE_SPEED:
        result = change_wav_speed(audio_data)

    if op == CHANGE_TYPE_SLOWER:
        result = change_wav_slower(audio_data)

    if op == CHANGE_TYPE_HIGHER:
        result = change_wav_higher(audio_data)

    if op == CHANGE_TYPE_LOWER:
        result = change_wav_lower(audio_data)

    if op == CHANGE_TYPE_LOW_PASS:
        result = change_wav_low_pass(audio_data)

    return sample_rate, result


def change_file():
    """
    Starts menu to change exising WAV file.
    First gets the name of the files and tries
    to convert it to an array. then presents
    menu of options, and calls the modifying
    function accordingly
    :return: audio sample rate and data
    """
    #  Get file name
    file_name = input('Enter wav file name: ')

    if not os.path.isfile(file_name):
        print("The file does not exist.")
        return -1

    result = load_wave(file_name)

    if result == -1:
        print("The file is not a valid wav file.")
        return -1

    sample_rate, audio_data = result[0], result[1]
    return change_wav(sample_rate, audio_data)


def read_file_lines(filename):
    """
    Returns array of all the lines in filename
    :param filename: path to file
    :return: array of all lines
    """

    f = open(filename, 'r')
    lines = [i for i in f.readlines()]
    f.close()

    return lines


def composite_wav():
    """
    Asks for composite instructions, and if it
    is a valid file, it creates an audio data
    array by the instructions and returns it.
    :return: audio data array and sample rate
    """

    #  Get file name
    file_name = input('Enter instructions file name: ')

    if not os.path.isfile(file_name):
        print("The file does not exist.")
        return -1

    #  Check if the file is valid

    file_content = "".join(read_file_lines(file_name))
    values = file_content.split(" ")
    values_len = len(values)

    #  Check if we can build a valid instructions
    #  from values

    if len(values) % 2 != 0:
        print("Bad format of instruction file.")
        return -1

    instructions = list()

    for i in range(0, int(values_len/2)):
        pos = 2*i
        inst = [values[pos], values[pos+1]]

        if inst[0] not in INSTRUCTION_LIST or not inst[1].isnumeric():
            print("Bad format of instructions file.")
            return -1

        instructions.append(inst)

    #  Build the result array
    result = list()

    for inst in instructions:
        #  The length of the instruction frequency
        length = int(COMPOSITE_SAMPLE_RATE/16 * int(inst[1]))
        freq = FREQUENCIES[inst[0]]

        samples_per_cycle = COMPOSITE_SAMPLE_RATE/freq

        for i in range(0, length):
            val = int(MAX_VOLUME * math.sin(2 * math.pi * i / samples_per_cycle))
            result.append([val, val])

    return COMPOSITE_SAMPLE_RATE, result


def combine_wav():
    """
    Combines two WAV file to one (puts it on one another)
    first gets file names, reads them, calculated mutual frame_rate
    and uses merge_data to merge them.
    :return: frame rate and data array
    """

    #  Gets files
    file = input("Enter files to combine: ")
    file = file.split(' ')
    file1 = file[0]
    file2 = file[1]

    #  Loads data
    frame_rate1, data1 = load_wave(file1)
    frame_rate2, data2 = load_wave(file2)

    #  Merge algorithm
    frame_rate = min(frame_rate1, frame_rate2)
    gc = great_calculator_divider(frame_rate1, frame_rate2)
    if frame_rate1 < frame_rate2:
        data = merge_data(data1, data2, gc, frame_rate1, frame_rate2)
    else:
        data = merge_data(data2, data1, gc, frame_rate2, frame_rate1)

    return frame_rate, data


def great_calculator_divider(a, b):
    """
    Returns the highest value that a and b
    divides by it together
    :param a: int
    :param b: int
    :return: the gcd
    """
    for i in range(1, 1 + min(a, b)):
        if a % i == 0 and b % i == 0:
            gc = i
    return gc


def merge_data(data1, data2, gc, ft1, ft2):
    """
    Merge two WAV data arrays when ft1 < ft2.
    :param data1: WAV data array
    :param data2: WAV data array
    :param gc: gcd for ft1, ft2
    :param ft1: Frame rate of data1
    :param ft2: Frame rate of data2
    :return: combined data
    """

    #  From every ft2/gc values from data2
    #  Get ft1/gc values from data2 and combine
    #  with ft1/gc values from data1

    data = []
    c = int(abs((ft1 - ft2)) / gc)
    j = -1
    k = 0
    for i in range(len(data1)):
        j += 1
        if j >= len(data2):
            break
        data.append([int(0.5 * (data1[i][0] + data2[j][0])),
                     int(0.5 * (data1[i][1] + data2[j][1]))])

        if k >= ft1 / gc-1:
            j += c
            k = -1
        k += 1

    #  If there are more items after the combine in
    #  data1 or in data2, continue taking ft2/gc
    #  items from ft1/gc items in data2
    if i >= len(data1)-1:
        while j < len(data2):
            j += 1
            if j >= len(data2):
                break

            data.append([int(data2[j][0]), int(data2[j][1])])

            if k >= ft1 / gc-1:
                j += c
                k = -1

            k += 1

        return data

    #  If there are items left in data1, just add them.
    if j >= len(data2):
        while i < len(data1):
            data.append([int(data1[i][0]), int(data1[i][1])])
            i += 1

    return data


def save_file(sample_rate, result):
    """
    Gets name for output file and saves
    the generated output file.
    :param sample_rate: sample rate of generated
    WAV file.
    :param result: audio data array
    :return:
    """

    file_name = input("Enter output file name: ")

    save_wave(sample_rate, result, file_name)


def save_menu(sample_rate, result):
    """
    Shows save options for the WAV file,
    and executes them.
    :param sample_rate: sample rate of generated
    WAV file.
    :param result: audio data array OR 0 if saved
        OR -1 at error
    :return:
    """

    #  Show save menu as long as the user
    #  doesn't enter a valid operation
    while True:
        print("Available operations: ")
        print("    1. Save WAV file")
        print("    2. Change WAV file")

        op = input(">> ")

        if op in SAVE_INDEXES:
            #  The user entered right operation
            break

        print("Not valid operation.")
        print()

    #  Modify the WAV file
    if op == SAVE_OP_CHANGE:
        result = change_wav(sample_rate, result)
        return result

    #  Save file and return to main menu
    if op == SAVE_OP_SAVE:
        save_file(sample_rate, result)
        return 0


def start_menu():
    """
    Show start options for the WAV file,
    and executes them.
    :return: 1 on exit, 0 on restart menu
    """

    print("Available operations: ")
    print("    1. Change WAV file")
    print("    2. Combine WAV files")
    print("    3. Composite WAV file")
    print("    4. Exit the program")

    print("")

    index = input(">> ")

    if index not in START_INDEXES:
        print("Operation not available.")
        #  Display operations again
        return 0

    if index == START_OP_CHANGE:
        result = change_file()

    if index == START_OP_COMBINE:
        result = combine_wav()

    if index == START_OP_COMPOSITE:
        result = composite_wav()

    if index == START_OP_EXIT:
        print("Bye!")
        return 1

    while result != -1 and result != 0:
        result = save_menu(result[0], result[1])

    #  If error occured
    if result == -1:
        return 1

    return 0


def full_main():
    result = 0

    #  User wants to show start menu
    #  again
    while result == 0:
        result = start_menu()
        print()

    pass

if __name__ == "__main__":
    full_main()
