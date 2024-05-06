'''
This is the main file that will be used to run the program.
It will be used to run the program and test the functions that are created in the other files.
'''
from helper_functions import to_grey_code, from_grey_code, to_binary, from_binary

number = 2315263271
number_grey = to_grey_code(number)
print(f"Gray code of {number} is {number_grey}")
number_back = from_grey_code(number_grey)
print(f"Back to decimal: {number_back}")

binary = to_binary(number)
print(f"Binary of {number} is {binary}")
number_back = from_binary(binary)
print(f"Back to decimal: {number_back}")
