'''
This file contains the functions that map the input bits to the corresponding symbols.
'''

import numpy as np


def coh_bpsk_demapper(noisy_bpsk):
    output_bits = np.zeros(len(noisy_bpsk))
    for i in range(len(noisy_bpsk)):
        if noisy_bpsk[i] > 0:
            output_bits[i] = 1
        elif noisy_bpsk[i] <= 0:
            output_bits[i] = 0
    return output_bits

def qbsk_demapper(input_bits):
    '''
    This function maps the input bits to the corresponding Q-PSK symbols.
    '''
    demodulation_bits = np.zeros(len(input_bits) * 2)
    for i in range(len(input_bits)):
        k = i * 2
        if input_bits[i].real > 0:
            demodulation_bits[k] = 0
        else:
            demodulation_bits[k] = 1

        if input_bits[i].imag > 0:
            demodulation_bits[k + 1] = 0
        else:
            demodulation_bits[k + 1] = 1

    return demodulation_bits
    

def psk_8_demapper(noisy_psk_8):
    '''
    This function maps the input bits to the corresponding 8-PSK symbols.
    '''
    output_bits = np.zeros(len(noisy_psk_8) * 3)
    
    for i in range(len(noisy_psk_8)):
        angle_rad = np.angle(noisy_psk_8[i])
        if angle_rad >= - np.pi/8 and angle_rad <  np.pi/8:
            output_bits[3*i] = 0
            output_bits[3*i + 1] = 0
            output_bits[3*i + 2] = 0
        elif angle_rad >=  np.pi/8 and angle_rad < 3*np.pi/8:
            output_bits[3*i] = 0
            output_bits[3*i + 1] = 0
            output_bits[3*i + 2] = 1
        elif angle_rad >= 3*np.pi/8 and angle_rad < 5*np.pi/8:
            output_bits[3*i] = 0
            output_bits[3*i + 1] = 1
            output_bits[3*i + 2] = 1
        elif angle_rad >= 5*np.pi/8 and angle_rad < 7*np.pi/8:
            output_bits[3*i] = 0
            output_bits[3*i + 1] = 1
            output_bits[3*i + 2] = 0
        elif angle_rad >= 7*np.pi/8 or angle_rad < -7*np.pi/8:
            output_bits[3*i] = 1
            output_bits[3*i + 1] = 1
            output_bits[3*i + 2] = 0
        elif angle_rad >= -7*np.pi/8 and angle_rad < -5*np.pi/8:
            output_bits[3*i] = 1
            output_bits[3*i + 1] = 1
            output_bits[3*i + 2] = 1
        elif angle_rad >= -5*np.pi/8 and angle_rad < -3*np.pi/8:
            output_bits[3*i] = 1
            output_bits[3*i + 1] = 0
            output_bits[3*i + 2] = 1
        elif angle_rad >= -3*np.pi/8 and angle_rad < -np.pi/8:
            output_bits[3*i] = 1
            output_bits[3*i + 1] = 0
            output_bits[3*i + 2] = 0
    return output_bits

def coh_ook_demapper(input_bits):
    '''
    This function maps the input bits to the corresponding OOK symbols.
    '''
    modulation_bits = np.zeros(len(input_bits), dtype = complex)
    for i in range(len(input_bits)):
        if input_bits[i] > 0.5:
            modulation_bits[i] = 1
        else:
            modulation_bits[i] = 0
            
    return modulation_bits

def coh_ask_8_demapper(input_bits):
    '''
    This function maps the 8-ASK symbols to the corresponding output bits.
    '''
    output_bits = np.zeros(len(input_bits) * 3)
    for i in range(len(input_bits)):
        K = i * 3
        if input_bits[i].real > 0 and input_bits[i].real < 2:
            output_bits[K] = output_bits[K + 1] = output_bits[K + 2] = 0
        elif input_bits[i].real >= 2 and input_bits[i].real < 4:
            output_bits[K] = output_bits[K + 1] = 0
            output_bits[K + 2] = 1
        elif input_bits[i].real >= 4 and input_bits[i].real < 6:
            output_bits[K] = 0
            output_bits[K + 1] = output_bits[K + 2] = 1
        elif input_bits[i].real >= 6:
            output_bits[K] = output_bits[K + 2] = 0
            output_bits[K + 1] = 1
        elif input_bits[i].real < 0 and input_bits[i].real > -2:
            output_bits[K] = 0
            output_bits[K + 1] = output_bits[K + 2] = 1
        elif input_bits[i].real <= -2 and input_bits[i].real > -4:
            output_bits[K] = output_bits[K + 2] = 1
            output_bits[K + 1] = 0
        elif input_bits[i].real <= -4 and input_bits[i].real > -6:
            output_bits[K] = output_bits[K + 1] = output_bits[K + 2] = 1
        elif input_bits[i].real <= -6:
            output_bits[K] = output_bits[K + 1] = 1
            output_bits[K + 2] = 0

    return output_bits
            
            
    
def qam_demapper(noisy_qam_4):
    output_bits = np.zeros(len(noisy_qam_4) * 2)
    for i in range(len(noisy_qam_4)):
        if noisy_qam_4[i].real > 0:
            output_bits[2*i] = 1
        else:
            output_bits[2*i] = 0
            
        if noisy_qam_4[i].imag > 0:
            output_bits[2*i + 1] = 1
        else:
            output_bits[2*i + 1] = 0
    return output_bits

def qam_8_demapper(noisy_qam_8):
    '''
    This function maps the input bits to the corresponding 8-QAM symbols.
    '''
    output_bits = np.zeros(len(noisy_qam_8) * 3)
    for i in range(len(noisy_qam_8)):
        K = i * 3
        if noisy_qam_8[i].real < 0:
            output_bits[K] = 0
        else:
            output_bits[K] = 1

        if noisy_qam_8[i].imag < 0:
            output_bits[K + 2] = 0
        else:
            output_bits[K + 2] = 1

        if noisy_qam_8[i].real < 2 and noisy_qam_8[i].real >= -2:
            output_bits[K + 1] = 1
        else:
            output_bits[K + 1] = 0

    return output_bits

def qam_16_demapper(noisy_qam_16):
    '''
    This function maps the input bits to the corresponding 16-QAM symbols.
    '''
    output_bits = np.zeros(len(noisy_qam_16) * 4)
    for i in range(len(noisy_qam_16)):
        #real part
        if noisy_qam_16[i].real < -2:
            output_bits[4*i] = 0
            output_bits[4*i + 1] = 0
        elif noisy_qam_16[i].real < 0 and noisy_qam_16[i].real >= -2:
            output_bits[4*i] = 0
            output_bits[4*i + 1] = 1
        elif noisy_qam_16[i].real >= 0 and noisy_qam_16[i].real < 2:
            output_bits[4*i] = 1
            output_bits[4*i + 1] = 1
        elif noisy_qam_16[i].real >= 2:
            output_bits[4*i] = 1
            output_bits[4*i + 1] = 0

        #imaginary part
        if noisy_qam_16[i].imag < -2:
            output_bits[4*i + 2] = 0
            output_bits[4*i + 3] = 0
        elif noisy_qam_16[i].imag < 0 and noisy_qam_16[i].imag >= -2:
            output_bits[4*i + 2] = 0
            output_bits[4*i + 3] = 1
        elif noisy_qam_16[i].imag >= 0 and noisy_qam_16[i].imag < 2:
            output_bits[4*i + 2] = 1
            output_bits[4*i + 3] = 1
        elif noisy_qam_16[i].imag >= 2:
            output_bits[4*i + 2] = 1
            output_bits[4*i + 3] = 0
    return output_bits

def coh_bfsk_demapper(input_bits):
    '''
    This function maps the input bits to the corresponding BFSK symbols.
    '''
    demodulation_bits = np.zeros(len(input_bits))
    for i in range(len(input_bits)):
        if input_bits[i].real > input_bits[i].imag:
            demodulation_bits[i] = 1
        else:
            demodulation_bits[i] = 0

    return demodulation_bits

def diff_bpsk_mapper():
    '''
    This function maps the input bits to the corresponding differentially encoded BPSK symbols.
    '''
    print("not implemened")
