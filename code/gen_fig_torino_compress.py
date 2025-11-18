import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft

data_path1 = '../data/Compress_U/'
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



repeaties = [4, 8, 12, 16, 20]
nodes = [0, 75, 76, 100, 140, 200]

dt = 0.1

#plot torino
exact_ms = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')
exact_ms = exact_ms[:160]
Sz_name_torino = 'ibm_torino_mid_Szs_x2.txt'
ref_name_torino = 'ibm_torino_ref_x2.txt'
data_s = get_data(Sz_name_torino, 1)
ref_s = get_data(ref_name_torino, 1)

cnt = len(exact_ms)
ts = np.arange(0, dt*cnt, dt)
plt.plot(ts, exact_ms, 'k--', label='exact')
cnt = len(data_s)
ts = np.arange(dt, dt*(cnt+1), dt)
plt.plot(ts, data_s, marker = 'o', markersize = 5,linestyle = 'None', label = r'$\langle \sigma^z_\mathrm{cen}\rangle$')
plt.plot(ts, ref_s, marker = 's', markersize = 6, markerfacecolor='none', linestyle = 'None', label = 'ref')
val = []
for i in range(cnt):
    val.append(-data_s[i]/ref_s[i])
plt.plot(ts, val, marker = '^', markersize = 5, label = 'mitigated')
plt.legend(loc = 'lower right')
for i in range(len(repeaties)):
    rep = repeaties[i]
    start = nodes[i]*dt
    if i != 1 and i != 0:
        plt.axvline(x=start, linestyle = '--', linewidth = 1, color = 'gray')
plt.ylim([-1.25, 0.0])
plt.text(3, -0.1, '9 layers', fontsize=10)
plt.text(7.7, -0.1, '25 layers', fontsize=10)
plt.text(11, -0.06, '33 layers', fontsize=10)
plt.text(14, -0.1, '41 layers', fontsize=10)
plt.xlabel('$t$')
plt.ylabel(r'$\langle\sigma^z_\mathrm{cen}\rangle$')
plt.savefig(fig_path + 'ibm_torino_compress.pdf')
plt.show()
plt.close()




