import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

data_path = '../data/N8_exact/'
fig_path = '../figs/'

dt = 0.1

# PRL-like style
plt.rcParams.update({
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "lines.linewidth": 1.0,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# Single-column figure, top-bottom panels
fig, axs = plt.subplots(2, 1, figsize=(3.4, 4.8))

# =========================
# Load data
# =========================
exact_ms_D4 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')
exact_ms_D2 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUUDDUUU.npy')
exact_ms_D0 = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUUUUUUU.npy')

cnt = len(exact_ms_D4)
ts = np.arange(0, dt * cnt, dt)

# =========================
# (a) time evolution
# =========================
ax = axs[0]

ax.text(
    -0.22, 1.02, '(a)',
    transform=ax.transAxes,
    fontsize=8,
    ha='left',
    va='bottom',
    clip_on=False
)

ax.plot(
    ts, exact_ms_D4,
    'o-', markersize=2.3,
    label=r'$|\uparrow\uparrow\downarrow\downarrow\downarrow\downarrow\uparrow\uparrow\rangle$'
)
ax.plot(
    ts, exact_ms_D2,
    's-', markersize=1.8,
    label=r'$|\uparrow\uparrow\uparrow\downarrow\downarrow\uparrow\uparrow\uparrow\rangle$'
)
ax.plot(
    ts, exact_ms_D0,
    '^-', markersize=1.8,
    label=r'$|\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\rangle$'
)

ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}}(t) \rangle$')
ax.tick_params(direction='in', top=True, right=True)
ax.legend(loc='upper right', bbox_to_anchor=(1.02, 0.8), fontsize=8)

# =========================
# (b) frequency spectrum
# =========================
ax = axs[1]

ax.text(
    -0.22, 1.02, '(b)',
    transform=ax.transAxes,
    fontsize=8,
    ha='left',
    va='bottom',
    clip_on=False
)

l = 100
ms_D4_cut = exact_ms_D4[:l]
ms_D2_cut = exact_ms_D2[:l]
ms_D0_cut = exact_ms_D0[:l]

cnt = len(ms_D4_cut)
f = fftfreq(cnt, dt)

mf_D4 = fft(ms_D4_cut)
mf_D2 = fft(ms_D2_cut)
mf_D0 = fft(ms_D0_cut)

freq = f[1:int(len(f) / 2)]

ax.semilogy(
    freq, abs(mf_D4[1:int(len(mf_D4) / 2)]),
    'o-', markersize=2.5,
    label=r'$|\uparrow\uparrow\downarrow\downarrow\downarrow\downarrow\uparrow\uparrow\rangle$'
)
ax.semilogy(
    freq, abs(mf_D2[1:int(len(mf_D2) / 2)]),
    's-', markersize=2.3,
    label=r'$|\uparrow\uparrow\uparrow\downarrow\downarrow\uparrow\uparrow\uparrow\rangle$'
)
ax.semilogy(
    freq, abs(mf_D0[1:int(len(mf_D0) / 2)]),
    '^-', markersize=2.3,
    label=r'$|\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\uparrow\rangle$'
)

ax.set_ylim(0.0, 70)

m1 = 1.0
m2 = 1.6180339887 * m1
m3 = 1.9890437907 * m1

for x in [m2 - m1, m1, m2, m3, m1 + m2]:
    ax.axvline(x=x, linestyle='--', linewidth=0.8, color='gray')

ax.text(m2 - m1 - 0.50, 20, r'$m_2-m_1$', fontsize=7)
ax.text(m1 + 0.02, 10, r'$m_1$', fontsize=7)
ax.text(m2 + 0.02, 5, r'$m_2$', fontsize=7)
ax.text(m3 + 0.02, 1.2, r'$m_3$', fontsize=7)
ax.text(m1 + m2 + 0.02, 0.7, r'$m_1+m_2$', fontsize=7)

ax.set_xlabel(r'$\omega / 2\pi$')
ax.set_ylabel(r'$\langle\sigma^z_{\mathrm{cen}}(\omega)\rangle$')
ax.tick_params(direction='in', top=True, right=True)
ax.legend(loc='upper right', bbox_to_anchor=(1.05, 1.0), fontsize=8)

# Layout
plt.tight_layout(pad=0.5)
plt.subplots_adjust(
    left=0.22,
    right=0.96,
    top=0.96,
    bottom=0.12,
    hspace=0.24
)

plt.savefig(
    fig_path + 'initial_diff_simulator.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.02
)

plt.show()
plt.close()
