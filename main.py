'''
This is the main file that will be used to run the program.
It will be used to run the program and test the functions that are created in the other files.
'''
from helper_functions import to_grey_code, from_grey_code, to_binary, from_binary
import mapper, channel, demapper
import numpy as np
from scipy import special
import matplotlib.pyplot as plt

# mapped_qam_8_bits = mapper.qam_8_mapper(number)
# number_grey = to_grey_code(0b010)
#print(f"Gray code of 010 is {to_binary(number_grey)}")
ber_simulated_bpsk = []
ber_simulated_qpsk = []
ber_simulated_8_psk = []
ber_simulated_ook = []
ber_simulated_8_ask = []
ber_simulated_qam =[]
ber_simulated_8_qam = []
ber_simulated_16_qam = []
ber_simulated_bfsk = []
ber_simulated_dpsk = []

arr = [1, 1, 0, 0, 1, 1, 1, 1, 1, 0]
number = np.random.randint(0, 2, 48000)
mapped_bpsk_bits = mapper.coh_bpsk_mapper(number)
mapped_qpsk_bits = mapper.qpsk_mapper(number)
mapped_8_psk_bits = mapper.psk_8_mapper(number)
mapped_ook_bits = mapper.coh_ook_mapper(number)
mapped_8_ask_bits = mapper.coh_ask_8_mapper(number)
mapped_qam_bits = mapper.qam_mapper(number)
mapped_8_qam_bits = mapper.qam_8_mapper(number)
mapped_16_qam_bits = mapper.qam_16_mapper(number)
mapped_bfsk_bits = mapper.coh_bfsk_mapper(number)
mapped_dpsk_bits = mapper.diff_psk_mapper(number)

# print(mapped_8_ask_bits)
# print(demapper.coh_ask_8_demapper(mapped_8_ask_bits))
theoretical_bpsk = []
theoretical_qpsk = []
theoretical_8_psk = []
theoretical_ook = []
theoretical_8_ask = []
theoretical_qam = []
theoretical_8_qam = []
theoretical_16_qam = []
theoretical_bfsk = []
theoretical_dfsk = []

dpsk_Pe = []

for i in range(-2,11):

    # BPSK
    channel_bpsk = channel.generate_channel(mapped_bpsk_bits, i, 1)
    demapped_bpsk_bits = demapper.coh_bpsk_demapper(channel_bpsk)
    ber_simulated_bpsk.append(np.sum(np.abs(np.array(number) - np.array(demapped_bpsk_bits)))/len(number))
    theoretical_bpsk.append(0.5 * special.erfc(np.sqrt(10 ** (i/10))))

    # QPSK
    channel_qpsk = channel.generate_channel(mapped_qpsk_bits, i, 2)
    demapped_qpsk_bits = demapper.qpsk_demapper(channel_qpsk)
    ber_simulated_qpsk.append(np.sum(np.abs(np.array(number) - np.array(demapped_qpsk_bits)))/len(number))
    qpsk_average_energy = channel.energy_average(mapped_qpsk_bits)
    qpsk_energy_symbol = channel.energy_symbol(2,qpsk_average_energy)
    theoretical_qpsk.append(0.5 * special.erfc(np.sqrt(10 ** (i/10))))

    # 8-PSK
    channel_8_psk = channel.generate_channel(mapped_8_psk_bits, i, 3)
    demapped_8_psk_bits = demapper.psk_8_demapper(channel_8_psk)
    ber_simulated_8_psk.append(np.sum(np.abs(np.array(number) - np.array(demapped_8_psk_bits)))/len(number))
    theoretical_8_psk.append(special.erfc(np.sqrt(3 * 10 ** (i/10)) * np.sin(np.pi/8)) / 3)

    # OOK
    channel_ook = channel.generate_channel(mapped_ook_bits, i, 1)
    demapped_ook_bits = demapper.coh_ook_demapper(channel_ook)
    ber_simulated_ook.append(np.sum(np.abs(np.array(number) - np.array(demapped_ook_bits)))/len(number))
    theoretical_ook.append(0.5 * special.erfc(np.sqrt(10 ** (i/10) / 2)))

    # 8-ASK
    channel_8_ask = channel.generate_channel(mapped_8_ask_bits, i, 3)
    demapped_8_ask_bits = demapper.coh_ask_8_demapper(channel_8_ask)
    ber_simulated_8_ask.append(np.sum(np.abs(np.array(number) - np.array(demapped_8_ask_bits)))/len(number))
    theoretical_8_ask.append(7 * special.erfc(np.sqrt(10 ** (i/10)/7)) / (3*8))

    # QAM
    channel_qam = channel.generate_channel(mapped_qam_bits, i, 2)
    demapped_qam_bits = demapper.qam_demapper(channel_qam)
    ber_simulated_qam.append(np.sum(np.abs(np.array(number) - np.array(demapped_qam_bits)))/len(number))
    theoretical_qam.append(0.5 * special.erfc(np.sqrt(10 ** (i/10))))

    # 8-QAM
    channel_8_qam = channel.generate_channel(mapped_8_qam_bits, i, 3)
    demapped_qam_8_bits = demapper.qam_8_demapper(channel_8_qam)
    ber_simulated_8_qam.append(np.sum(np.abs(np.array(number) - np.array(demapped_qam_8_bits)))/len(number))
    theoretical_8_qam.append(5 * special.erfc(np.sqrt(10 ** (i/10) / 2)) / 12)

    # 16-QAM
    channel_16_qam = channel.generate_channel(mapped_16_qam_bits, i, 4)
    demapped_16_qam_bits = demapper.qam_16_demapper(channel_16_qam)
    ber_simulated_16_qam.append(np.sum(np.abs(np.array(number) - np.array(demapped_16_qam_bits)))/len(number))
    theoretical_16_qam.append(3 * special.erfc(np.sqrt(10 ** (i/10) / 2.5)) / 8)

    # BFSK
    channel_bfsk = channel.generate_channel(mapped_bfsk_bits, i, 1)
    demapped_bfsk_bits = demapper.coh_bfsk_demapper(channel_bfsk)
    ber_simulated_bfsk.append(np.sum(np.abs(np.array(number) - np.array(demapped_bfsk_bits)))/len(number))
    theoretical_bfsk.append(0.5 * special.erfc(np.sqrt(10 ** (i/10) / 2)))

    # DPSK
    channel_dpsk = channel.generate_channel(mapped_dpsk_bits, i, 1)
    demapped_dpsk_bits = demapper.diff_psk_demapper(np.real(np.array(channel_dpsk)))
    ber_simulated_dpsk.append(np.sum(np.abs(np.array(number) - np.array(demapped_dpsk_bits))) / len(number))
    dpsk_Pe.append(special.erfc(np.sqrt(10 ** (i/10))) - (special.erfc(np.sqrt(10 ** (i/10))) ** 2) / 2)

    
plt.semilogy(range(-2,11), ber_simulated_bpsk)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for BPSK")
plt.semilogy(range(-2,11), theoretical_bpsk)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_qpsk)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for QPSK")
plt.semilogy(range(-2,11), theoretical_qpsk)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_8_psk)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for 8-PSK")
plt.semilogy(range(-2,11), theoretical_8_psk)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_ook)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for OOK")
plt.semilogy(range(-2,11), theoretical_ook)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_8_ask)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for 8-ASK")
plt.semilogy(range(-2,11), theoretical_8_ask)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_qam)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for QAM")
plt.semilogy(range(-2,11), theoretical_qam)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_8_qam)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for 8-QAM")
plt.semilogy(range(-2,11), theoretical_8_qam)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_16_qam)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for 16-QAM")
plt.semilogy(range(-2,11), theoretical_16_qam)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_bfsk)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for BFSK")
plt.semilogy(range(-2,11), theoretical_bfsk)
plt.show()

plt.semilogy(range(-2,11), ber_simulated_dpsk)
plt.xlabel("SNR")
plt.ylabel("BER")
plt.title("BER vs SNR for DFSK")
plt.semilogy(range(-2,11), dpsk_Pe)
plt.show()

