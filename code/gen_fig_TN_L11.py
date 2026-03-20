import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, ifft

data_path = '../data/TN_res_data/'
fig_path = '../figs/'
init_state = 'UUDDDDDDDUU'

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
file_exact = data_path + file_exact
ms_exact = (np.load(file_exact))
cnt = len(ms_exact)
ts = np.arange(0, dt*cnt, dt)
#time

fig, axs = plt.subplots(1, 2, figsize=(11, 4))  # 1 row, 2 columns

cnt_exact = len(ms_exact)
ts = np.arange(0, dt*cnt_exact, dt)



# Plot on first subplottext
axs[0].text(-0.18, 1.1, '(a)', transform=axs[0].transAxes, fontsize=14, verticalalignment='top')
axs[0].plot(ts, ms_exact)
title = '$J=' + '{:g}'.format(J) + ', h_x=' + '{:g}'.format(hx) + ', h_z=' + '{:g}'.format(hz) +\
        ', L='+str(N) +'$, '+ '\ninit=' + init_state
#axs[0].set_title(title)
axs[0].set_xlabel('$t$')
axs[0].set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}}\rangle$')

# Plot on second subplot

#freq
f_exact = fftfreq(cnt_exact, dt)
mf_exact = fft(ms_exact)
#plt.figure().set_figwidth(7.2)
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
axs[1].text(-0.15, 1.1, '(b)', transform=axs[1].transAxes, fontsize=14, verticalalignment='top')
axs[1].semilogy(f_exact[1:int(len(f_exact)/2)], abs(mf_exact[1:int(len(mf_exact)/2)]), color = 'k')

alpha = 0.7
axs[1].axvline(x = m21, color = cycle[0], linestyle='--', label = '$m_2-m_1$', alpha = alpha)
axs[1].axvline(x = m1, color = 'k', linestyle = '--', label = '$m_1=$'+str(m1), alpha = alpha)
axs[1].axvline(x = m22, color = cycle[1],linestyle = '--',  label = '$2m_1$', alpha = alpha)
axs[1].axvline(x = m12,color = cycle[2],linestyle = '--',  label = '$m_1+m_2$', alpha = alpha)
axs[1].axvline(x = m2,color = cycle[3],linestyle = '--',  label = '$m_2$', alpha = alpha)
axs[1].axvline(x = m3,color = cycle[4],linestyle = '--',  label = '$m_3$', alpha = alpha)
axs[1].axvline(x = m4,color = cycle[5],linestyle = '--',  label = '$m_4$', alpha = alpha)
axs[1].axvline(x = m5,color = cycle[6],linestyle = '--',  label = '$m_5$', alpha = alpha)
axs[1].axvline(x = m13,color = cycle[7],linestyle = '--',  label = '$m_1+m_3$', alpha = alpha)
axs[1].axvline(x = m33,color = cycle[8],linestyle = '--',  label = '$3m_1$', alpha = alpha)
axs[1].axvline(x = m6,color = cycle[9],linestyle = '--',  label = '$m_6$', alpha = alpha)
axs[1].axvline(x = m222,color = cycle[0],linestyle = '-.',  label = '$2m_2$', alpha = alpha)
axs[1].axvline(x = m7,color = cycle[1],linestyle = '-.',  label = '$m_7$', alpha = alpha)
axs[1].axvline(x = m8,color = cycle[2],linestyle = '-.',  label = '$m_8$', alpha = alpha)

axs[1].set_xlim([0,5])
axs[1].set_ylim([0,100])

axs[1].text(0.56-0.12, 40, '0.56', fontsize=10)
axs[1].text(0.96-0.02, 3, '0.96', fontsize=10)
axs[1].text(1.51-0.12, 0.5, '1.51', fontsize=10)
axs[1].text(1.99-0.08, 0.13, '1.99', fontsize=10)
axs[1].text(2.55-0.12, 0.2, '2.55', fontsize=10)
#ax = plt.subplot(111)
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
axs[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
#axs[1].legend(loc='upper right')
#plt.title(title)
axs[1].set_xlabel('$\omega / 2\pi$')
axs[1].set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}}\rangle$')


# Adjust layout
plt.tight_layout()
plt.subplots_adjust(wspace=0.3)  # Increase horizontal spacing

plt.savefig(fig_path + 'L11_E8.pdf')
plt.show()
plt.close()

