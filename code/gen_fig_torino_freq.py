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



dt = 0.1


fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.8))  # 1 row, 3 columns

exact_ms = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')


#plot trotter torino, compress torino, D4
Sz_name_torino_trotter_x2 = 'ibm_torino_mid_Szs_x2_fix_layout.txt'
ref_name_torino_trotter_x2 = 'ibm_torino_ref_x2_fix_layout.txt'
exact_ms_D4 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')
Sz_name_torino_x2 = 'ibm_torino_mid_Szs_x2.txt'
ref_name_torino_x2 = 'ibm_torino_ref_x2.txt'
data_trotter = get_data(Sz_name_torino_trotter_x2, 2)
ref_trotter = get_data(ref_name_torino_trotter_x2, 2)
data_com = get_data(Sz_name_torino_x2, 1)
ref_com = get_data(ref_name_torino_x2, 1)
l = 100

## FFT
exact_ms_D4 = exact_ms_D4[:l]
data_trotter = data_trotter[:l]
data_com = data_com[:l]
f_exact = fftfreq(len(exact_ms_D4), dt)
f_trotter = fftfreq(len(data_trotter), dt)
f_com = fftfreq(len(data_com), dt)
mf_exact = fft(exact_ms_D4)
mf_trotter = fft(data_trotter)
mf_com = fft(data_com)
axs[0].text(-0.15, 1.1, '(a)', transform=axs[0].transAxes, fontsize=14, verticalalignment='top')
axs[0].semilogy(f_exact[1:int(len(f_exact)/2)], abs(mf_exact[1:int(len(mf_exact)/2)]), marker = 'o', color = 'k', label = 'exact')
axs[0].semilogy(f_trotter[1:int(len(f_trotter)/2)], abs(mf_trotter[1:int(len(mf_trotter)/2)]), marker = 's', label = 'ibm_torino trotter', linestyle='none')
axs[0].semilogy(f_com[1:int(len(f_com)/2)], abs(mf_com[1:int(len(mf_com)/2)]), marker = '^', label = 'ibm_torino compressed', linestyle='none')
m1 = 1.
m2 = 1.6180339887 * m1
m3 = 1.9890437907 * m1
m4 = 2.4048671724 * m1
axs[0].axhline(y=70, linestyle = '--', linewidth = 1, color = 'gray')
axs[0].axvline(x=(m2-m1), ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[0].axvline(x=m1, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[0].axvline(x=m2, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[0].axvline(x=m3, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[0].axvline(x=m1+m2, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[0].set_title(r'initial state = $\left| \uparrow \uparrow \downarrow \downarrow \downarrow \downarrow \uparrow \uparrow \right\rangle$')
axs[0].set_xlabel('$\omega$')
axs[0].set_ylabel(r'$\langle \sigma^z_\mathrm{cen}\rangle$')
axs[0].set_ylim([0.008, 200])
axs[0].arrow( m2-m1 - 0.12, 40, 0, -15, linewidth = 2, head_width=0.1, head_length=4, fc='r',  ec='r', zorder = 10)
axs[0].text( m2-m1 - 0.5, 100, "$m_{2-1}$", fontsize=10, color='k')
axs[0].text( m1 - 0.1, 100, "$m_{1}$", fontsize=10, color='k')
axs[0].text( m2 - 0.2, 100, "$m_{2}$", fontsize=10, color='k')
axs[0].text( m3 - 0.1, 100, "$m_{3}$", fontsize=10, color='k')
axs[0].text( m1+m2 - 0.3, 100, "$m_{1+2}$", fontsize=10, color='k')



#plot trotter torino, compress torino, D2
Sz_name_torino_trotter_x3 = 'ibm_torino_mid_Szs_x3_fix_layout.txt'
ref_name_torino_trotter_x3 = 'ibm_torino_ref_x3_fix_layout.txt'
exact_ms_D2 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUUDDUUU.npy')
Sz_name_torino_x3 = 'ibm_torino_mid_Szs_x3.txt'
ref_name_torino_x3 = 'ibm_torino_ref_x3.txt'
data_trotter = get_data(Sz_name_torino_trotter_x3, 2)
ref_trotter = get_data(ref_name_torino_trotter_x3, 2)
data_com = get_data(Sz_name_torino_x3, 1)
ref_com = get_data(ref_name_torino_x3, 1)
l = 100

cnt = len(exact_ms_D2)
ts = np.arange(0, dt*cnt, dt)

## FFT
exact_ms_D2 = exact_ms_D2[:l]
data_trotter = data_trotter[:l]
data_com = data_com[:l]
f_exact = fftfreq(len(exact_ms_D2), dt)
f_trotter = fftfreq(len(data_trotter), dt)
f_com = fftfreq(len(data_com), dt)
mf_exact = fft(exact_ms_D2)
mf_trotter = fft(data_trotter)
mf_com = fft(data_com)
axs[1].text(-0.08, 1.1, '(b)', transform=axs[1].transAxes, fontsize=14, verticalalignment='top')
axs[1].semilogy(f_exact[1:int(len(f_exact)/2)], abs(mf_exact[1:int(len(mf_exact)/2)]), marker = 'o', color = 'k', label = 'exact')
axs[1].semilogy(f_trotter[1:int(len(f_trotter)/2)], abs(mf_trotter[1:int(len(mf_trotter)/2)]), marker = 's', label = 'ibm_torino trotter', linestyle='none')
axs[1].semilogy(f_com[1:int(len(f_com)/2)], abs(mf_com[1:int(len(mf_com)/2)]), marker = '^', label = 'ibm_torino compressed', linestyle='none')
m1 = 1.
m2 = 1.6180339887 * m1
m3 = 1.9890437907 * m1
m4 = 2.4048671724 * m1
axs[1].axhline(y=70, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=(m2-m1), ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m1, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m2, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m3, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m1+m2, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
#axs[1].legend(loc = 'best')
axs[1].set_title(r'initial state = $\left| \uparrow \uparrow \uparrow \downarrow \downarrow \uparrow \uparrow \uparrow \right\rangle$')
axs[1].set_xlabel('$\omega$')
axs[1].set_ylim([0.008, 200])
axs[1].arrow( m2-m1-0.12, 10, 0, -4, linewidth = 2, head_width=0.1, head_length=1.2, fc='r',  ec='r', zorder = 10)
axs[1].arrow( m1, 13, 0, -5, linewidth = 2, head_width=0.1, head_length=1.5, fc='r',  ec='r', zorder = 10)
axs[1].arrow( m2, 5, 0, -2, linewidth = 2, head_width=0.1, head_length=0.5, fc='r',  ec='r', zorder = 10)
axs[1].text( m2-m1 - 0.5, 100, "$m_{2-1}$", fontsize=10, color='k')
axs[1].text( m1 - 0.1, 100, "$m_{1}$", fontsize=10, color='k')
axs[1].text( m2 - 0.2, 100, "$m_{2}$", fontsize=10, color='k')
axs[1].text( m3 - 0.1, 100, "$m_{3}$", fontsize=10, color='k')
axs[1].text( m1+m2 - 0.3, 100, "$m_{1+2}$", fontsize=10, color='k')
axs[1].set_yticks([])

#plot trotter torino, compress torino, D0
Sz_name_torino_trotter_x0 = 'ibm_torino_mid_Szs_x0_fix_layout.txt'
ref_name_torino_trotter_x0 = 'ibm_torino_ref_x0_fix_layout.txt'
exact_ms_D0 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUUUUUUU.npy')
Sz_name_torino_x0 = 'ibm_torino_mid_Szs_x0.txt'
ref_name_torino_x0 = 'ibm_torino_ref_x0.txt'
data_trotter = get_data(Sz_name_torino_trotter_x0, 2)
ref_trotter = get_data(ref_name_torino_trotter_x0, 2)
data_com = get_data(Sz_name_torino_x0, 1)
ref_com = get_data(ref_name_torino_x0, 1)
l = 100

cnt = len(exact_ms_D0)
ts = np.arange(0, dt*cnt, dt)

val = []
for i in range(len(data_trotter)):
    val.append(data_trotter[i]/ref_trotter[i])
data_trotter = val
val = []
for i in range(len(data_com)):
    val.append(data_com[i]/ref_com[i])
data_com = val

cnt = len(data_trotter)
ts = np.arange(dt, dt*(cnt+1), dt)

## FFT
exact_ms_D0 = exact_ms_D0[:l]
data_trotter = data_trotter[:l]
data_com = data_com[:l]
f_exact = fftfreq(len(exact_ms_D0), dt)
f_trotter = fftfreq(len(data_trotter), dt)
f_com = fftfreq(len(data_com), dt)
mf_exact = fft(exact_ms_D0)
mf_trotter = fft(data_trotter)
mf_com = fft(data_com)
axs[2].text(-0.08, 1.1, '(c)', transform=axs[2].transAxes, fontsize=14, verticalalignment='top')
axs[2].semilogy(f_exact[1:int(len(f_exact)/2)], abs(mf_exact[1:int(len(mf_exact)/2)]), marker = 'o', color = 'k', label = 'exact')
axs[2].semilogy(f_trotter[1:int(len(f_trotter)/2)], abs(mf_trotter[1:int(len(mf_trotter)/2)]), marker = 's', label = '$1^{\mathrm{st}}$ Trotter', linestyle='none')
axs[2].semilogy(f_com[1:int(len(f_com)/2)], abs(mf_com[1:int(len(mf_com)/2)]), marker = '^', label = 'Riemannian opt', linestyle='none')

m1 = 1.
m2 = 1.6180339887 * m1
m3 = 1.9890437907 * m1
m4 = 2.4048671724 * m1
axs[2].axhline(y=70, linestyle = '--', linewidth = 1, color = 'gray')
axs[2].axvline(x=(m2-m1), ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[2].axvline(x=m1, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[2].axvline(x=m2, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[2].axvline(x=m3, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[2].axvline(x=m1+m2, ymax = 0.9, linestyle = '--', linewidth = 1, color = 'gray')
axs[2].legend(loc='upper right', bbox_to_anchor=(1.24, 1.01))
axs[2].set_xlabel('$\omega$')
axs[2].set_ylim([0.008, 200])
axs[2].set_title(r'initial state = $\left| \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \right\rangle$')
axs[2].arrow( m1, 5, 0, -2, linewidth = 2, head_width=0.1, head_length=0.6, fc='r',  ec='r', zorder = 10)
axs[2].arrow( m2, 8, 0, -3.5, linewidth = 2, head_width=0.1, head_length=0.8, fc='r',  ec='r', zorder = 10)
axs[2].arrow( m1+m2, 2.2, 0, -1, linewidth = 2, head_width=0.1, head_length=0.2, fc='r',  ec='r', zorder = 10)
axs[2].text( m2-m1 - 0.5, 100, "$m_{2-1}$", fontsize=10, color='k')
axs[2].text( m1 - 0.1, 100, "$m_{1}$", fontsize=10, color='k')
axs[2].text( m2 - 0.2, 100, "$m_{2}$", fontsize=10, color='k')
axs[2].text( m3 - 0.1, 100, "$m_{3}$", fontsize=10, color='k')
axs[2].text( m1+m2 - 0.3, 100, "$m_{1+2}$", fontsize=10, color='k')
axs[2].set_yticks([])
plt.tight_layout()
plt.subplots_adjust(wspace=0.1)  # Increase horizontal spacing
plt.savefig(fig_path + 'torino_trotter_compressed_FFT.pdf')
plt.show()
#plt.close()
