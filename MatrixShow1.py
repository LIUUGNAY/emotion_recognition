import pickle
from matplotlib import pyplot as plt
# import pandas as pd
import pylab as pl

import numpy as np
# from scpy2.pandas import plot_dataframe_as_colormesh
process = 'D:/python/预处理数据集/data_PCCMatrix_python/s01/s09.dat'
# process1 = 'D:/python/预处理数据集/data_SubBand_python/s01/s09.dat'
s = open(process, "rb")
# s1 = open(process1, "rb")
num = pickle.load(s, encoding="latin1")
# num1 = pickle.load(s1, encoding="latin1")

def plot_dataframe_as_colormesh(df, ax=None, inverse_yaxis=False, colorbar=False, xtick_rot=0,
                   xtick_start=0, xtick_step=1, ytick_start=0, ytick_step=1,
                   xtick_format=None, ytick_format=None,
                   **kw):
    nrow, ncol = df.shape
    if ax is None:
        fig_width = 10.0
        fig_height = fig_width / ncol * nrow
        fig, ax = pl.subplots(figsize=(fig_width, fig_height))

    ax.set_aspect("equal")
    if inverse_yaxis:
        ax.invert_yaxis()
    mesh = ax.pcolormesh(df, **kw)
    if colorbar:
        pl.colorbar(ax=ax, mappable=mesh)

    xticks_loc = np.arange(xtick_start, ncol, xtick_step)
    yticks_loc = np.arange(ytick_start, nrow, ytick_step)

    xlabels = df.tolist()
    if xtick_format is not None:
        xlabels = [xtick_format(label) for label in xlabels]
    ylabels = df.tolist()
    if ytick_format is not None:
        ylabels = [ytick_format(label) for label in ylabels]

    ax.set_xticks(xticks_loc + 0.5)
    ax.set_xticklabels([xlabels[idx] for idx in xticks_loc], rotation=xtick_rot)
    ax.set_yticks(yticks_loc + 0.5)
    ax.set_yticklabels([ylabels[idx] for idx in yticks_loc])
    return ax





Theta = num['Alpha_pccMatrix']
fig, ax = pl.subplots()
plot_dataframe_as_colormesh(Theta, ax=ax, colorbar=True, xtick_rot=90)
plt.imshow(Theta)
plt.show()



