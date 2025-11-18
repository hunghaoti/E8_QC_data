import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, ifft

data_path = '../data/diff_N_exact/'
fig_path = '../figs/'
init_states = [
    'UUUUUUUUUUU',
]
init_states = [
    'UUDDU',
    'UUUDDUUU',
    'UUUUUUUUUUUUUDDUUUUUUUUUUUU'
]

dt = 0.1
for init_state in init_states:
    N = len(init_state)
    ms = np.load(data_path + 'N'+str(N)+'_'+init_state+'_m.npy')
    cnt = len(ms)
    ts = np.arange(0, dt*cnt, dt)
    #freq
    f = fftfreq(cnt, dt)
    mf = fft(ms)
    if N == 27:
        plt.semilogy(f[1:int(len(f)/2)], abs(mf[1:int(len(mf)/2)]), ':k', label = r'$L='+str(N) +'$')
    else:
        plt.semilogy(f[1:int(len(f)/2)], abs(mf[1:int(len(mf)/2)]), label = r'$L='+str(N) +'$')
    #plt.title('L='+str(N)+',Initial state = ' + init_state)
    plt.xlabel('$\omega$')
    plt.ylabel(r'$\langle \sigma^z_\mathrm{cen}\rangle$')
plt.legend(loc = 'upper right')
plt.savefig(fig_path + 'diff_sites.pdf')
plt.show()


