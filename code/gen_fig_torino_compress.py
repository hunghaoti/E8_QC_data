import numpy as np
import matplotlib.pyplot as plt

data_path1 = '../data/Compress_U/'
data_path2 = '../data/trotter/'
data_path = '../data/N8_exact/'
fig_path = '../figs/'

def get_data(file_name, idx):
    data_path_tmp = data_path1 if idx == 1 else data_path2
    with open(data_path_tmp + file_name, "r") as file:
        Szs = [float(line.strip()) for line in file.readlines()]
    return Szs

repeaties = [4, 8, 12, 16, 20]
nodes = [0, 75, 76, 100, 140, 200]

dt = 0.1

# PRL-like style
plt.rcParams.update({
    "font.size": 7,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "lines.linewidth": 1.0,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

# Data
exact_ms = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')[:160]

Sz_name_torino = 'ibm_torino_mid_Szs_x2.txt'
ref_name_torino = 'ibm_torino_ref_x2.txt'
data_s = get_data(Sz_name_torino, 1)
ref_s = get_data(ref_name_torino, 1)

cnt_exact = len(exact_ms)
ts_exact = np.arange(0, dt * cnt_exact, dt)

cnt = len(data_s)
ts_data = np.arange(dt, dt * (cnt + 1), dt)

val = [-data_s[i] / ref_s[i] for i in range(cnt)]

# Single-column PRL figure
fig, ax = plt.subplots(figsize=(3.4, 2.9))

ax.plot(
    ts_exact, exact_ms,
    'k--',
    label='Exact'
)

ax.plot(
    ts_data, data_s,
    marker='o',
    markersize=2.5,
    linestyle='None',
    label=r'$\langle \sigma^z_{\mathrm{cen}} \rangle$'
)

ax.plot(
    ts_data, ref_s,
    marker='s',
    markersize=3.2,
    markerfacecolor='none',
    linestyle='None',
    label='Ref'
)

ax.plot(
    ts_data, val,
    marker='^',
    markersize=2.8,
    linestyle='-',
    label='Mitigated'
)

# Vertical separators for layer changes
for i in range(len(repeaties)):
    start = nodes[i] * dt
    if i not in [0, 1]:
        ax.axvline(x=start, linestyle='--', linewidth=0.8, color='gray')

ax.set_ylim([-1.25, 0.0])
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}} \rangle$')
ax.tick_params(direction='in', top=True, right=True)

# Layer labels
ax.text(3.0, -0.10, '9 layers', fontsize=6)
ax.text(7.7, -0.10, '25 layers', fontsize=6)
ax.text(11.0, -0.06, '33 layers', fontsize=6)
ax.text(14.0, -0.10, '41 layers', fontsize=6)

ax.legend(
    loc='lower right',
    frameon=True,
    handlelength=1.6,
    borderpad=0.2,
    labelspacing=0.25
)

plt.tight_layout(pad=0.4)
plt.subplots_adjust(left=0.16, right=0.96, top=0.96, bottom=0.14)

plt.savefig(
    fig_path + 'ibm_torino_compress.pdf',
    dpi=300,
    bbox_inches='tight',
    pad_inches=0.02
)

plt.show()
plt.close()
