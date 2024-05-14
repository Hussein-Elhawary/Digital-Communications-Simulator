'''
root(NO*Evag/2*nb) = Noise 
'''
import numpy as np
def energy_average(complex_bits):
    # import numpy as np

    return np.mean(np.abs(complex_bits) ** 2)

def energy_symbol(nb, avg_energy):

    return nb / avg_energy

def Nsymbols(Es, No):

    return No / Es

def noise_signal(Ns, size):
    return np.random.randn(size) * np.sqrt(Ns / 2) + 1j * np.random.randn(size) * np.sqrt(Ns / 2)

# def generate_channel(nb, avg_energy, size):
#     Eavg = energy_average(nb)
#     Es = energy_symbol(nb, avg_energy)
#     No = Nsymbols(Es, 1)
#     Ns = No * Es
#     noise_signal = noise(Ns, size)
#     return noise_signal

def generateVariance(complex_bits, noiseValue, nb):
    No = 10 **  (-noiseValue / 10)
    Eb = energy_average(complex_bits) / nb # 3dd el bits
    No_over_2 = No / 2 * Eb
    return No_over_2

def generate_channel(complex_bits, noiseValue, nb):
    No_over_2 = generateVariance(complex_bits, noiseValue, nb)
    noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
    return complex_bits + noise_signal

# def coh_bpsk_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 1)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal

# def qpsk_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 2)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal

# def psk_8_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 3)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal

# def coh_ook_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 1)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal

# def coh_ask_8_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 3)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal

# def qam_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 4)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal

# def qam_8_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 3)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal

# def qam_16_channel(complex_bits, noiseValue):
#     No_over_2 = generateVariance(complex_bits, noiseValue, 4)
#     noise_signal = np.random.randn(len(complex_bits)) * np.sqrt(No_over_2) + 1j * np.random.randn(len(complex_bits)) * np.sqrt(No_over_2)
#     return complex_bits + noise_signal




