import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft

data_path1 = '../data/Compress_U/'
data_path = '../data/N8_exact/'
fig_path = '../figs/'

def get_data(file_name):
    print(data_path1 + file_name)
    with open(data_path1 + file_name, "r") as file:
        Szs = file.readlines()  # Reads all lines into a list
        Szs = [float(line.strip()) for line in Szs]  # Removes newline characters
    val = []
    for i in range(len(Szs)):
        #val.append(Szs[i]/Ref[i])
        val.append(Szs[i])
    return val

dt = 0.1

#layers = [4, 8, 12, 16, 20]
layers = [4, 20]
fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.8))  # 1 row, 2 columns
labels = ['a', 'b']
keep_len = 175
for i in range(len(layers)):
    layer = layers[i]
    label = labels[i]
    ax1 = axs[i]
    ax1.text(-0.18, 1.1, '(' + labels[i] + ')', transform=ax1.transAxes, fontsize=14, verticalalignment='top')
    exact_ms = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')
    exact_ms = exact_ms[:keep_len]
    #Sz_name = 'qasm_simulator_mid_Szs_lay' + str(layer) + '_2.txt'
    Sz_name = 'MPO_full_mid_Szs_lay' + str(layer) + '.txt'
    data_s = get_data(Sz_name)
    data_s = data_s[:keep_len]
    opt_errs = np.load(data_path1 + 'MPO_full_opt_err_layer' + str(layer) + '.npy')
    opt_errs = opt_errs[:keep_len]

    cnt = len(exact_ms)
    ts = np.arange(0, dt*cnt, dt)
    ax1.plot(ts, exact_ms, 'k--', label='exact')
    ts = np.arange(dt, dt*(cnt+1), dt)
    ax1.plot(ts, data_s, 'b-', marker = 'o', label='Compress U', markersize = 5)
    ax1.set_ylim([-1.0, 0.5])
    ax1.set_xlabel('t')
    ax1.set_ylabel(r'$\langle\sigma^z_\mathrm{cen}\rangle}$', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.legend(loc = 'upper left')

    ax2 = ax1.twinx()
    ax2.semilogy(ts, opt_errs, 'r', label='error', markersize = 5)
    ax2.set_ylabel('$C_F$', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    ax2.legend(loc = 'upper right')
    #plt.xlim([-0.1, 17.5])
    plt.ylim([1.0e-10, 2.0e1])
    real_layers = 2*layer + 1
    plt.title(str(real_layers) + ' layers')
plt.tight_layout()
plt.subplots_adjust(wspace=0.4)  # Increase horizontal spacing

plt.savefig(fig_path + 'MPO_full_rep.pdf')
plt.show()
plt.close()





