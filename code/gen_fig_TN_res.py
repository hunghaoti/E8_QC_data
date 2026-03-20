import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

data_path = '../data/TN_res_data/'
fig_path = '../figs/'
init_state = 'UUDDDDUU'

dt = 0.1
J = 1
hx = 1.0
hz = 3.0

m1 = 0.956
m22 = 2 * m1
m2 = m1 * 1.618
m12 = m1 + m2
m21 = m2 - m1
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

file_exact = (
    data_path + 'exact/' +
    'Szs_' + 'J_' + '{:g}'.format(J) +
    '_hx_' + '{:g}'.format(hx) +
    '_hz_' + '{:g}'.format(hz) +
    '_N' + str(N) + '_' + init_state + '.npy'
)
file_tdvp = data_path + 'tdvp/' + 'Szs_tdvp_N' + str(N) + '_' + init_state + '.npy'
file_trotter = data_path + 'trotter/' + 'N' + str(N) + '_' + init_state + '_m.npy'

ms_exact = np.load(file_exact)
ms_tdvp = np.load(file_tdvp)
ms_trotter = np.load(file_trotter)

# PRL-like style
plt.rcParams.update({
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7,
    "lines.linewidth": 1.0,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# Single-column figure, stacked panels
fig, axs = plt.subplots(2, 1, figsize=(3.4, 4.8))

# =========================
# (a) time evolution
# =========================
ax = axs[0]

cnt_trotter = len(ms_trotter)
ts_trotter = np.arange(0, dt * cnt_trotter, dt)

cnt_tdvp = len(ms_tdvp)
ts_tdvp = np.arange(0, dt * cnt_tdvp, dt)

cnt_exact = len(ms_exact)
ts_exact = np.arange(0, dt * cnt_exact, dt)

ax.text(
    -0.22, 1.02, '(a)',
    transform=ax.transAxes,
    fontsize=8,
    ha='left',
    va='bottom',
    clip_on=False
)

ax.plot(ts_trotter, ms_trotter, label=r'$1^{\mathrm{st}}$ Trotter decomposition')
ax.plot(ts_tdvp, ms_tdvp, label='TDVP')
ax.plot(ts_exact, ms_exact, linestyle='dashed', color='black', label='Exact')

ax.set_ylim([-1.05, 0.0])
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}}(t) \rangle$')
ax.tick_params(direction='in', top=True, right=True)
ax.legend(loc='upper right', frameon=True)

# =========================
# (b) frequency spectrum
# =========================
ax = axs[1]

f_exact = fftfreq(cnt_exact, dt)
mf_exact = fft(ms_exact)

f_trotter = fftfreq(cnt_trotter, dt)
mf_trotter = fft(ms_trotter)

f_tdvp = fftfreq(cnt_tdvp, dt)
mf_tdvp = fft(ms_tdvp)

ax.text(
    -0.22, 1.02, '(b)',
    transform=ax.transAxes,
    fontsize=8,
    ha='left',
    va='bottom',
    clip_on=False
)

ax.semilogy(
    f_trotter[1:int(len(f_trotter) / 2)],
    abs(mf_trotter[1:int(len(mf_trotter) / 2)]),
    label=r'$1^{\mathrm{st}}$ Trotter decomposition'
)

ax.semilogy(
    f_tdvp[1:int(len(f_tdvp) / 2)],
    abs(mf_tdvp[1:int(len(mf_tdvp) / 2)]),
    label='TDVP'
)

ax.semilogy(
    f_exact[1:int(len(f_exact) / 2)],
    abs(mf_exact[1:int(len(mf_exact) / 2)]),
    color='black',
    linestyle='dashed',
    label='Exact'
)

ax.set_xlim([0, 5])
ax.set_xlabel(r'$\omega / 2\pi$')
ax.set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}} (\omega)\rangle$')
ax.tick_params(direction='in', top=True, right=True)
ax.legend(loc='upper right', frameon=True)

# Layout
plt.tight_layout(pad=0.5)
plt.subplots_adjust(
    left=0.20,
    right=0.96,
    top=0.96,
    bottom=0.12,
    hspace=0.24
)

plt.savefig(
    fig_path + 'tdvp_trotter_N8.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.02
)

plt.show()
plt.close()
