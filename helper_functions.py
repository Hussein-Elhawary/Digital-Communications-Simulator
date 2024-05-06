'''
This file contains helper functions that are used in other files.
'''

def to_grey_code(decimal)->int:
    '''
    This function converts the input decimal number to its corresponding gray decimal.
    '''

    return decimal ^ (decimal >> 1)

def from_grey_code(grey_code)->int:
    '''
    This function converts the input gray decimal to its corresponding decimal number.
    '''

    mask = grey_code >> 1
    while mask != 0:
        grey_code = grey_code ^ mask
        mask = mask >> 1
    return grey_code

def to_binary(number)->int:
    '''
    This function converts the input number to its corresponding binary.
    '''
    return bin(number)[2:]

def from_binary(binary)->int:
    '''
    This function converts the input binary to its corresponding number.
    '''
    return int(binary, 2)

def random_binary_string(length:int)->str:
    '''
    This function generates a random binary string of the given length.
    '''
    import random
    return ''.join(random.choice(['0', '1']) for _ in range(length))