'''
This file contains the functions that map the input bits to the corresponding symbols.
'''

import numpy as np

def coh_bpsk_mapper(input_bits):
    modulation_bits = np.zeros(len(input_bits))
    
    for i in range(len(input_bits)):
        if input_bits[i] == 0:
            modulation_bits[i] = -1
        else:
            modulation_bits[i] = 1
    return modulation_bits

def qpsk_mapper(input_bits):
    modulation_bits = np.zeros(len(input_bits) // 2, dtype = complex)
    
    for i in range(0, len(input_bits), 2):
        k = i // 2
        if input_bits[i] == 0 and input_bits[i + 1] == 0:
            modulation_bits[k] = -1 - 1j
        elif input_bits[i] == 0 and input_bits[i + 1] == 1:
            modulation_bits[k] = -1 + 1j
        elif input_bits[i] == 1 and input_bits[i + 1] == 0:
            modulation_bits[k] = 1 - 1j
        elif input_bits[i] == 1 and input_bits[i + 1] == 1:
            modulation_bits[k] = 1 + 1j
    
    return modulation_bits
    

def psk_8_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding 8-PSK symbols.
    '''
    import math
    modulation_bits = np.zeros(len(input_bits) // 3, dtype = complex)
    for i in range(0, len(input_bits), 3):
        k = i // 3
        if input_bits[i] == 0 and input_bits[i + 1] == 0 and input_bits[i + 2] == 0:
            modulation_bits[k] = 1
        elif input_bits[i] == 0 and input_bits[i + 1] == 0 and input_bits[i + 2] == 1:
            modulation_bits[k] = math.cos(math.pi / 4) + (1j * math.sin(math.pi / 4))
        elif input_bits[i] == 0 and input_bits[i + 1] == 1 and input_bits[i + 2] == 1:
            modulation_bits[k] = 1j
        elif input_bits[i] == 0 and input_bits[i + 1] == 1 and input_bits[i + 2] == 0:
            modulation_bits[k] = - math.cos(math.pi / 4) + (1j * math.sin(math.pi / 4))
        elif input_bits[i] == 1 and input_bits[i + 1] == 1 and input_bits[i + 2] == 0:
            modulation_bits[k] = -1
        elif input_bits[i] == 1 and input_bits[i + 1] == 1 and input_bits[i + 2] == 1:
            modulation_bits[k] = - math.cos(math.pi / 4) - (1j * math.sin(math.pi / 4))
        elif input_bits[i] == 1 and input_bits[i + 1] == 0 and input_bits[i + 2] == 1:
            modulation_bits[k] = -1j
        elif input_bits[i] == 1 and input_bits[i + 1] == 0 and input_bits[i + 2] == 0:
            modulation_bits[k] = math.cos(math.pi / 4) - (1j * math.sin(math.pi / 4))

    return modulation_bits

def coh_ook_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding OOK symbols.
    '''
    return input_bits

def coh_ask_8_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding 8-ASK symbols.
    '''
    modulation_bits = np.zeros(len(input_bits) // 3, dtype = complex)
    for i in range(0, len(input_bits), 3):
        k = i // 3
        if input_bits[i] == 0 and input_bits[i + 1] == 0 and input_bits[i + 2] == 0:
            modulation_bits[k] = 1
        elif input_bits[i] == 0 and input_bits[i + 1] == 0 and input_bits[i + 2] == 1:
            modulation_bits[k] = 3
        elif input_bits[i] == 0 and input_bits[i + 1] == 1 and input_bits[i + 2] == 0:
            modulation_bits[k] = 7
        elif input_bits[i] == 0 and input_bits[i + 1] == 1 and input_bits[i + 2] == 1:
            modulation_bits[k] = 5
        elif input_bits[i] == 1 and input_bits[i + 1] == 0 and input_bits[i + 2] == 0:
            modulation_bits[k] = -1
        elif input_bits[i] == 1 and input_bits[i + 1] == 0 and input_bits[i + 2] == 1:
            modulation_bits[k] = -3
        elif input_bits[i] == 1 and input_bits[i + 1] == 1 and input_bits[i + 2] == 0:
            modulation_bits[k] = -7
        elif input_bits[i] == 1 and input_bits[i + 1] == 1 and input_bits[i + 2] == 1:
            modulation_bits[k] = -5

    return modulation_bits

def qam_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding QAM symbols.
    '''
    modulation_bits = np.zeros(len(input_bits) // 2, dtype = complex)
    for i in range(0, len(input_bits), 2):
        k = i // 2
        if input_bits[i] == 0 and input_bits[i + 1] == 0:
            real = -1
            imag = -1
        elif input_bits[i] == 0 and input_bits[i + 1] == 1:
            real = -1
            imag = 1
        elif input_bits[i] == 1 and input_bits[i + 1] == 0:
            real = 1
            imag = -1
        elif input_bits[i] == 1 and input_bits[i + 1] == 1:
            real = 1
            imag = 1
        
        modulation_bits[k] = real + (1j * imag)
    return modulation_bits


def qam_8_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding 8-QAM symbols.
    '''
    modulation_bits = np.zeros(len(input_bits) // 3, dtype = complex)
    for i in range(0, len(input_bits), 3):
        k = i // 3
        if input_bits[i] == 0 and input_bits[i + 1] == 0 and input_bits[i + 2] == 0:
            real = -3
            imag = -1
        elif input_bits[i] == 0 and input_bits[i + 1] == 0 and input_bits[i + 2] == 1:
            real = -3
            imag = 1
        elif input_bits[i] == 0 and input_bits[i + 1] == 1 and input_bits[i + 2] == 0:
            real = -1
            imag = -1
        elif input_bits[i] == 0 and input_bits[i + 1] == 1 and input_bits[i + 2] == 1:
            real = -1
            imag = 1
        elif input_bits[i] == 1 and input_bits[i + 1] == 0 and input_bits[i + 2] == 0:
            real = 3
            imag = -1
        elif input_bits[i] == 1 and input_bits[i + 1] == 0 and input_bits[i + 2] == 1:
            real = 3
            imag = 1
        elif input_bits[i] == 1 and input_bits[i + 1] == 1 and input_bits[i + 2] == 0:
            real = 1
            imag = -1
        elif input_bits[i] == 1 and input_bits[i + 1] == 1 and input_bits[i + 2] == 1:
            real = 1
            imag = 1
        
        modulation_bits[k] = real + (1j * imag)
        
    return modulation_bits

def qam_16_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding 16-QAM symbols.
    '''
    modulation_bits = np.zeros(len(input_bits) // 4, dtype = complex)
    for i in range(0, len(input_bits), 4):
        k = i // 4
        if input_bits[i] == 0 and input_bits[i + 1] == 0:
            real = -3
        elif input_bits[i] == 0 and input_bits[i + 1] == 1:
            real = -1
        elif input_bits[i] == 1 and input_bits[i + 1] == 0:
            real = 3
        elif input_bits[i] == 1 and input_bits[i + 1] == 1:
            real = 1
        
        if input_bits[i + 2] == 0 and input_bits[i + 3] == 0:
            imag = -3
        elif input_bits[i + 2] == 0 and input_bits[i + 3] == 1:
            imag = -1
        elif input_bits[i + 2] == 1 and input_bits[i + 3] == 0:
            imag = 3
        elif input_bits[i + 2] == 1 and input_bits[i + 3] == 1:
            imag = 1
        
        modulation_bits[k] = real + (1j * imag)
        
    return modulation_bits

def coh_bfsk_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding BFSK symbols.
    '''
    modulation_bits = np.zeros(len(input_bits), dtype = complex)
    for i in range(len(input_bits)):
        if input_bits[i] == 0:
            modulation_bits[i] = 1
        else:
            modulation_bits[i] = 1j

    return modulation_bits

def diff_psk_mapper(input_bits):
    '''
    This function maps the input bits to the corresponding differentially encoded BPSK symbols.
    '''
    new_input_bits = np.zeros(len(input_bits) + 1).astype(bool)
    new_input_bits[0] = 1
    input_bits = np.array(input_bits).astype(bool)
    for i in range(len(input_bits)):
        new_input_bits[i + 1] = np.bitwise_xor(new_input_bits[i], input_bits[i]).astype(bool)

    new_input_bits = coh_bpsk_mapper(new_input_bits)
    return new_input_bits.astype(int)
    

