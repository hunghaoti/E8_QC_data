import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft

data_path2 = '../data/trotter/'
data_path = '../data/N8_exact/'
fig_path = '../figs/'

def get_data(file_name, idx):
    data_path_tmp = data_path1 if idx == 1 else data_path2
    with open(data_path_tmp + file_name, "r") as file:
        Szs = [float(line.strip()) for line in file.readlines()]
    return Szs

dt = 0.1

# Explicit colors
color_exact = 'black'
color_data = 'tab:blue'
color_ref = 'orange'
color_ref2 = 'tab:green'
color_mitigated = 'tab:purple'

# Exact data
exact_ms = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')

# Trotter / reference data
Sz_name = 'ibm_torino_mid_Szs_x2_fix_layout.txt'
ref_name = 'ibm_torino_ref_x2_fix_layout.txt'
ref_name2 = 'ibm_torino_ref_x2_fix_layout_fix_rzz0.txt'

data_s = get_data(Sz_name, 2)
ref_s = get_data(ref_name, 2)
ref_s2 = get_data(ref_name2, 2)

# Mitigated
cnt = len(data_s)
val = [-data_s[i] / ref_s[i] for i in range(cnt)]

# Time arrays
cnt_exact = len(exact_ms)
ts_exact = np.arange(0, dt * cnt_exact, dt)
ts_data = np.arange(dt, dt * (cnt + 1), dt)

# PRL single-column style
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

# One single panel for one PRL column
fig, ax = plt.subplots(1, 1, figsize=(3.4, 2.7))

ax.plot(
    ts_exact, exact_ms,
    linestyle='--',
    color=color_exact,
    label='Exact'
)

ax.plot(
    ts_data, data_s,
    marker='o',
    linestyle='None',
    color=color_data,
    markersize=2.5,
    label=r'$\langle \sigma^z_{\mathrm{cen}} \rangle$'
)

ax.plot(
    ts_data, ref_s,
    marker='s',
    linestyle='None',
    color=color_ref,
    markerfacecolor='none',
    markersize=2.5,
    label='Ref, Rzz unchanged'
)

ax.plot(
    ts_data, ref_s2,
    marker='^',
    linestyle='None',
    color=color_ref2,
    markerfacecolor='none',
    markersize=2.5,
    label='Ref, all angles 0'
)

ax.plot(
    ts_data, val,
    marker='D',
    linestyle='-',
    color=color_mitigated,
    markersize=2.8,
    label='Mitigated'
)

ax.set_ylim([-1.2, 0.54])
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}} \rangle$')
ax.tick_params(direction='in', top=True, right=True)

ax.legend(
    loc='upper left',
    frameon=False,
    handlelength=1.6,
    borderpad=0.2,
    labelspacing=0.25
)

plt.tight_layout(pad=0.4)

plt.savefig(
    fig_path + 'torino_trotter.pdf',
    dpi=300,
    bbox_inches='tight'
)

plt.show()
plt.close()
