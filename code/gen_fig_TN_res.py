import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, ifft

data_path = '../data/TN_res_data/'
fig_path = '../figs/'
init_state = 'UUDDDDUU'

dt = 0.1
J = 1
#hxs = [0.0, 0.3, 0.8, 1.0, 1.2, 2.0]
hx = 1.
hz = 3.


m1 = 0.956
m22=2*m1
m2 = m1 * 1.618
m12=m1+m2
m21=m2-m1
m3 = m1 * 1.989
m4 = m1 * 2.405
m13 = m1 * 2.989
m5 = m1 * 2.956
m33 = m1 * 3
m6 = m1 * 3.218
m222 = m2 * 2
m7 = m1 * 3.891
m8 = m1 * 4.783

N = len(init_state)
file_exact = 'exact/' + 'Szs_' + 'J_' + '{:g}'.format(J)+ '_hx_' + '{:g}'.format(hx) + \
        '_hz_' + '{:g}'.format(hz) +'_N'+str(N)+'_'+init_state+'.npy'
file_tdvp = 'tdvp/' + 'Szs_tdvp_N'+str(N)+'_'+init_state+'.npy'
file_trotter = 'trotter/' + 'N'+str(N)+'_'+init_state+'_m.npy'
file_exact = data_path + file_exact
file_tdvp = data_path + file_tdvp
file_trotter = data_path + file_trotter
file_name2 = fig_path + file_exact
ms_exact = (np.load(file_exact))
ms_tdvp = (np.load(file_tdvp))
ms_trotter = (np.load(file_trotter))
cnt = len(ms_exact)
ts = np.arange(0, dt*cnt, dt)
#time
cnt_trotter = len(ms_trotter)
ts = np.arange(0, dt*cnt_trotter, dt)

fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.8))  # 1 row, 2 columns

axs[0].plot(ts, ms_trotter, label=r'$1^{\mathrm{st}}$ Trotter decomposition')
cnt_tdvp = len(ms_tdvp)
ts = np.arange(0, dt*cnt_tdvp, dt)
axs[0].plot(ts, ms_tdvp, label = 'TDVP')
cnt_exact = len(ms_exact)
ts = np.arange(0, dt*cnt_exact, dt)




# Plot on first subplottext
axs[0].text(-0.18, 1.1, '(a)', transform=axs[0].transAxes, fontsize=14, verticalalignment='top')
axs[0].plot(ts, ms_exact,linestyle = 'dashed', color = 'black', label = 'exact')
title = '$J=' + '{:g}'.format(J) + ', h_x=' + '{:g}'.format(hx) + ', h_z=' + '{:g}'.format(hz) +\
        ', L='+str(N) +'$, '+ '\ninit=' + init_state
axs[0].set_ylim([-1.05, 0])
#axs[0].set_title(title)
axs[0].legend(loc = 'upper left')
axs[0].set_xlabel('$t$')
axs[0].set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}}(t) \rangle$')

# Plot on second subplot

#freq
f_exact = fftfreq(cnt_exact, dt)
mf_exact = fft(ms_exact)
f_trotter = fftfreq(cnt_trotter, dt)
mf_trotter = fft(ms_trotter)
f_tdvp = fftfreq(cnt_tdvp, dt)
mf_tdvp = fft(ms_tdvp)
#plt.figure().set_figwidth(7.2)
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
axs[1].text(-0.15, 1.1, '(b)', transform=axs[1].transAxes, fontsize=14, verticalalignment='top')
#axs[1].axvline(x = m21, color = cycle[0], linestyle='--', label = '$m_2-m_1$')
#axs[1].axvline(x = m1, color = 'k', linestyle = '--', label = '$m_1=$'+str(m1))
#plt.axvline(x = m22, color = cycle[1],linestyle = '--',  label = '$2m_1$')
#axs[1].axvline(x = m12,color = cycle[2],linestyle = '--',  label = '$m_1+m_2$')
#axs[1].axvline(x = m2,color = cycle[3],linestyle = '--',  label = '$m_2$')
#axs[1].axvline(x = m3,color = cycle[4],linestyle = '--',  label = '$m_3$')
#plt.axvline(x = m4,color = cycle[5],linestyle = '--',  label = '$m_4$')
#plt.axvline(x = m5,color = cycle[6],linestyle = '--',  label = '$m_5$')
#plt.axvline(x = m13,color = cycle[7],linestyle = '--',  label = '$m_1+m_3$')
#plt.axvline(x = m33,color = cycle[8],linestyle = '--',  label = '$3m_1$')
#plt.axvline(x = m6,color = cycle[9],linestyle = '--',  label = '$m_6$')
#plt.axvline(x = m222,color = cycle[0],linestyle = '-.',  label = '$2m_2$')
#plt.axvline(x = m7,color = cycle[1],linestyle = '-.',  label = '$m_7$')
#plt.axvline(x = m8,color = cycle[2],linestyle = '-.',  label = '$m_8$')
axs[1].semilogy(f_trotter[1:int(len(f_trotter)/2)], abs(mf_trotter[1:int(len(mf_trotter)/2)]), label=r'$1^{\mathrm{st}}$ Trotter decomposition')
axs[1].semilogy(f_tdvp[1:int(len(f_tdvp)/2)], abs(mf_tdvp[1:int(len(mf_tdvp)/2)]), label = 'TDVP')
axs[1].semilogy(f_exact[1:int(len(f_exact)/2)], abs(mf_exact[1:int(len(mf_exact)/2)]), color = 'k', label = 'exact',linestyle = 'dashed')
axs[1].set_xlim([0,5])
#ax = plt.subplot(111)
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
axs[1].legend(loc='upper right')
#plt.title(title)
axs[1].set_xlabel('$\omega$')
axs[1].set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}}(\omega) \rangle$')


# Adjust layout
plt.tight_layout()
plt.subplots_adjust(wspace=0.4)  # Increase horizontal spacing

plt.savefig(fig_path + 'tdvp_trotter_N8.pdf')
plt.show()
plt.close()

