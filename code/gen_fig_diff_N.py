import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

data_path = '../data/diff_N_exact/'
fig_path = '../figs/'

init_states = [
    'UUDDU',
    'UUUDDUUU',
    'UUUUUUUUUUUUUDDUUUUUUUUUUUU'
]

dt = 0.1

# PRL style
plt.rcParams.update({
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 8,
    "lines.linewidth": 1.0,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# Single-column figure
fig, ax = plt.subplots(figsize=(3.4, 2.8))

for init_state in init_states:
    N = len(init_state)
    ms = np.load(data_path + 'N' + str(N) + '_' + init_state + '_m.npy')

    cnt = len(ms)
    f = fftfreq(cnt, dt)
    mf = fft(ms)

    freq = f[1:int(len(f) / 2)]
    amp = abs(mf[1:int(len(mf) / 2)])

    if N == 27:
        ax.semilogy(freq, amp, ':k', label=rf'$L={N}$')
    else:
        ax.semilogy(freq, amp, label=rf'$L={N}$')

ax.set_xlabel(r'$\omega / 2\pi$')

# FIXED y-label (important!)
ax.set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}}(\omega) \rangle$')

ax.tick_params(direction='in', top=True, right=True)

ax.legend(loc='upper right', frameon=False)

# Layout
plt.tight_layout(pad=0.4)
plt.subplots_adjust(left=0.18, right=0.96, top=0.96, bottom=0.14)

# Save high quality
plt.savefig(
    fig_path + 'diff_sites.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.02
)

plt.show()
plt.close()
