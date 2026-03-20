import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft

data_path1 = '../data/Compress_U/'
data_path = '../data/N8_exact/'
fig_path = '../figs/'

def get_data(file_name):
    print(data_path1 + file_name)
    with open(data_path1 + file_name, "r") as file:
        Szs = file.readlines()
        Szs = [float(line.strip()) for line in Szs]
    val = []
    for i in range(len(Szs)):
        val.append(Szs[i])
    return val

dt = 0.1
layers = [4, 20]
labels = ['a', 'b']
keep_len = 175

# PRL-like single-column figure size
# one column in PRL is roughly ~3.4 inches wide
fig, axs = plt.subplots(2, 1, figsize=(3.4, 4.6), sharex=True)

# optional style tuning
plt.rcParams.update({
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "lines.linewidth": 1.0,
})

for i in range(len(layers)):
    layer = layers[i]
    ax1 = axs[i]

    # panel label outside upper-left corner
    ax1.text(
        -0.30, 1.03, f'({labels[i]})',
        transform=ax1.transAxes,
        fontsize=10,
        ha='left',
        va='bottom',
        clip_on=False
    )

    exact_ms = np.load(data_path + 'Szs_J_1_hx_1_hz_3_N8_UUDDDDUU.npy')
    exact_ms = exact_ms[:keep_len]

    Sz_name = 'MPO_full_mid_Szs_lay' + str(layer) + '.txt'
    data_s = get_data(Sz_name)
    data_s = data_s[:keep_len]

    opt_errs = np.load(data_path1 + 'MPO_full_opt_err_layer' + str(layer) + '.npy')
    opt_errs = opt_errs[:keep_len]

    cnt = len(exact_ms)
    ts_exact = np.arange(0, dt * cnt, dt)
    ts_data = np.arange(dt, dt * (cnt + 1), dt)

    # left axis
    l1, = ax1.plot(ts_exact, exact_ms, 'k--', label='Exact')
    l2, = ax1.plot(ts_data, data_s, 'b-o', label='Compress U', markersize=2.5)

    ax1.set_ylim([-1.0, 0.5])
    ax1.set_ylabel(r'$\langle \sigma^z_{\mathrm{cen}} \rangle$', color = 'blue')
    ax1.tick_params(direction='in', top=True, right=False)
    ax1.tick_params(
        axis='y',
        colors='blue',      # ← y-ticks + tick labels
        direction='in'
    )

    # centered layer text inside panel
    real_layers = 2 * layer + 1
    ax1.text(
        0.8, 0.96, f'{real_layers} layers',
        transform=ax1.transAxes,
        fontsize=8,
        ha='center',
        va='top'
    )

    # right axis
    ax2 = ax1.twinx()
    l3, = ax2.semilogy(ts_data, opt_errs, 'r-', label=r'$C_F$')
    ax2.set_ylabel(r'$C_F$', color= 'r')
    ax2.set_ylim([1.0e-10, 8.0e1])
    ax2.tick_params(direction='in', top=True, right=True)
    ax2.tick_params(
        axis='y',
        colors='red',      # ← y-ticks + tick labels
        direction='in',
    )

    # compact legend
    lines = [l1, l2, l3]
    labels_legend = [line.get_label() for line in lines]
    ax1.legend(lines, labels_legend, loc='upper left', frameon=False,
               handlelength=1., borderpad=0.2, labelspacing=0.25)

axs[-1].set_xlabel(r'$t$')
axs[-1].set_xlim([0, ts_data[-1]])

plt.tight_layout(pad=0.5)
plt.subplots_adjust(left=0.20, right=0.84, top=0.96, bottom=0.12, hspace=0.16)

plt.savefig(fig_path + 'MPO_full_rep.pdf', bbox_inches='tight',dpi=300)
plt.show()
plt.close()
