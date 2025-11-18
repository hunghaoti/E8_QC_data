import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft

data_path2 = '../data/trotter/'
data_path = '../data/N8_exact/'
fig_path = '../figs/'

def get_data(file_name, idx):
    data_path_tmp = data_path1 if idx==1 else data_path2
    with open(data_path_tmp + file_name, "r") as file:
        Szs = file.readlines()  # Reads all lines into a list
        Szs = [float(line.strip()) for line in Szs]  # Removes newline characters
    val = []
    for i in range(len(Szs)):
        val.append(Szs[i])
    return val

dt = 0.1
#plot torino
exact_ms = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')
#plot trotter torino, with diff reference
Sz_name_torino_trotter_x2 = 'ibm_torino_mid_Szs_x2_fix_layout.txt'
ref_name_torino_trotter_x2 = 'ibm_torino_ref_x2_fix_layout.txt'
ref_name_torino_trotter_x2_rzz0 = 'ibm_torino_ref_x2_fix_layout_fix_rzz0.txt'
data_s = get_data(Sz_name_torino_trotter_x2, 2)
ref_s = get_data(ref_name_torino_trotter_x2, 2)
ref_s2 = get_data(ref_name_torino_trotter_x2_rzz0, 2)

cnt = len(exact_ms)
ts = np.arange(0, dt*cnt, dt)

fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.8))  # 1 row, 2 columns

axs[0].text(-0.18, 1.1, '(a)', transform=axs[0].transAxes, fontsize=14, verticalalignment='top')
axs[0].plot(ts, exact_ms, 'k--', label='exact')
cnt = len(data_s)
ts = np.arange(dt, dt*(cnt+1), dt)
axs[0].plot(ts, data_s, marker = 'o', markersize = 5, label = '$\langle \sigma^z_\mathrm{cen}\\rangle$')
axs[0].plot(ts, ref_s, marker = 's',linestyle = 'None', markerfacecolor='none', markersize = 6, label='ref, Rzz unchanged')
axs[0].plot(ts, ref_s2, marker = '^', linestyle = 'None', markersize = 6, markerfacecolor='none', label='ref, all angles 0')
axs[0].legend(loc = 'upper left')
val = []
for i in range(cnt):
    val.append(-data_s[i]/ref_s[i])
axs[0].set_xlabel('$t$')
axs[0].set_ylabel(r'$\langle\sigma^z_\mathrm{cen}\rangle$')

#plot trotter torino
axs[1].text(-0.15, 1.1, '(b)', transform=axs[1].transAxes, fontsize=14, verticalalignment='top')
data_s = get_data(Sz_name_torino_trotter_x2, 2)
ref_s = get_data(ref_name_torino_trotter_x2, 2)

cnt = len(exact_ms)
ts = np.arange(0, dt*cnt, dt)
axs[1].plot(ts, exact_ms, 'k--', label='exact')
cnt = len(data_s)
ts = np.arange(dt, dt*(cnt+1), dt)
axs[1].plot(ts, data_s, marker = 'o', markersize = 5,linestyle='None', label = '$\langle \sigma^z_\mathrm{cen}\\rangle$')
axs[1].plot(ts, ref_s, marker = 's',linestyle='None', markerfacecolor='none', markersize = 6, label='ref, Rzz unchanged')
val = []
for i in range(cnt):
    val.append(-data_s[i]/ref_s[i])
axs[1].plot(ts, val, marker = '^', markersize = 5, label = 'mitigated')
axs[1].legend(loc = 'upper left')
axs[1].set_xlabel('$t$')
axs[1].set_ylabel(r'$\langle\sigma^z_\mathrm{cen}\rangle$')
plt.tight_layout()
plt.subplots_adjust(wspace=0.3)  # Increase horizontal spacing
plt.savefig(fig_path + 'torino_trotter.pdf')
plt.show()
plt.close()

