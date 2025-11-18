import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft

data_path = '../data/N8_exact/'
fig_path = '../figs/'

dt = 0.1

fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.8))  # 1 row, 2 columns

#compare different inital state exact
exact_ms_D4 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')
exact_ms_D2 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUUDDUUU.npy')
exact_ms_D0 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUUUUUUU.npy')
cnt = len(exact_ms_D4)
ts = np.arange(0, dt*cnt, dt)
axs[0].text(-0.18, 1.1, '(a)', transform=axs[0].transAxes, fontsize=14, verticalalignment='top')
axs[0].plot(ts, exact_ms_D4, marker = 'o', markersize = 4, label = r'$\left| \uparrow \uparrow \downarrow \downarrow \downarrow \downarrow \uparrow \uparrow \right\rangle$')
axs[0].plot(ts, exact_ms_D2, marker = 's', markersize = 3, label = r'$\left| \uparrow \uparrow \uparrow \downarrow \downarrow \uparrow \uparrow \uparrow \right\rangle$')
axs[0].plot(ts, exact_ms_D0, marker = '^', markersize = 3, label = r'$\left| \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \right\rangle$')
axs[0].legend(loc='center right', bbox_to_anchor=(1.0, 0.6), fontsize=14)
axs[0].set_xlabel('$t$')
axs[0].set_ylabel(r'$\langle \sigma^z_\mathrm{cen}\rangle$')
#plt.savefig(fig_path + 'exact_diff_init.png')


#compare different inital state exact
l = 100
exact_ms_D4 = exact_ms_D4[:l]
exact_ms_D2 = exact_ms_D2[:l]
exact_ms_D0 = exact_ms_D0[:l]
cnt = len(exact_ms_D4)
f = fftfreq(cnt, dt)
mf_D4 = fft(exact_ms_D4)
mf_D2 = fft(exact_ms_D2)
mf_D0 = fft(exact_ms_D0)
axs[1].semilogy(f[1:int(len(f)/2)], abs(mf_D4[1:int(len(mf_D4)/2)]), marker = 'o', label = r'$\left| \uparrow \uparrow \downarrow \downarrow \downarrow \downarrow \uparrow \uparrow \right\rangle$')
axs[1].semilogy(f[1:int(len(f)/2)], abs(mf_D2[1:int(len(mf_D2)/2)]), marker = 's', label = r'$\left| \uparrow \uparrow \uparrow \downarrow \downarrow \uparrow \uparrow \uparrow \right\rangle$')
axs[1].semilogy(f[1:int(len(f)/2)], abs(mf_D0[1:int(len(mf_D0)/2)]), marker = '^', label = r'$\left| \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \uparrow \right\rangle$')
axs[1].legend(loc='best', framealpha=1.0, fontsize=14)
m1 = 1.
m2 = 1.6180339887 * m1
m3 = 1.9890437907 * m1
m4 = 2.4048671724 * m1
axs[1].text(-0.15, 1.1, '(b)', transform=axs[1].transAxes, fontsize=14, verticalalignment='top')
axs[1].axvline(x=(m2-m1), linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m1, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m2, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m3, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].axvline(x=m1+m2, linestyle = '--', linewidth = 1, color = 'gray')
axs[1].text(m2-m1-0.62, 17, '$m_2-m_1$', fontsize=10)
axs[1].text(m1+0.02, 10, '$m_1=1$', fontsize=10)
axs[1].text(m2+0.02, 5, '$m_2$', fontsize=10)
axs[1].text(m3+0.02, 1, '$m_3$', fontsize=10)
axs[1].text(m1+m2+0.02, 0.5, '$m_1+m_2$', fontsize=10)
axs[1].set_xlabel('$\omega$')
axs[1].set_ylabel(r'$\langle \sigma^z_\mathrm{cen}\rangle$')
plt.tight_layout()
plt.subplots_adjust(wspace=0.3)  # Increase horizontal spacing

plt.savefig(fig_path + 'initial_diff_simulator.pdf')
plt.show()
