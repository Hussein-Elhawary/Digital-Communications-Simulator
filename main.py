'''
This is the main file that will be used to run the program.
It will be used to run the program and test the functions that are created in the other files.
'''
from helper_functions import to_grey_code, from_grey_code, to_binary, from_binary
import numpy as np

number = np.random.randint(0, 2, 48000)
number_grey = to_grey_code(0b10010101)
print(f"Gray code of 010010101 is {to_binary(number_grey)}")



