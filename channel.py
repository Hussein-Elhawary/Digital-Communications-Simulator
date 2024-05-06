import numpy as np

#constants
SNR = np.arange(-2, 11, 1)
Eb_BPSK = 1
Eb_QPSK = 1
Eb_8PSK = 1/3
Eb_16QAM = 5/2


def BPSK_channel(modulation_bits, SNR):
    '''
    This function adds noise to the BPSK symbols.
    '''
    noisy_symbols = np.zeros(len(modulation_bits))
    noise = np.random.randn(len(modulation_bits))
    
    for i in range(len(SNR)):
        N0 = Eb_BPSK / SNR(i)
        sigma = np.sqrt(N0 / 2)
        noisy_symbols[i] = modulation_bits[i] + (sigma * noise[i])
        
    return noisy_symbols

# def awgn(signal, mean, variance):
#     from random import normal
#     noise = normal(mean, variance, len(signal))
#     return signal + noise


