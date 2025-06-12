import numpy
import os
from matplotlib import pyplot,patches,rcParams
from tqdm import tqdm
from scipy.linalg import solve
from scipy import interpolate
from scipy.integrate import quad
numpy.set_printoptions(precision=6)
# 3D plots
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


#################################################################################################
def latexify(fig_width=None, fig_height=None, columns=1):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    assert(columns in [1,2])

    if fig_width is None:
        fig_width = 3.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = (numpy.sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height + 
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES

    params = {'backend': 'ps',
              # 'text.latex.preamble' : [r'\usepackage{gensymb}'],
              'axes.labelsize': 10, # fontsize for x and y labels (was 10)
              'axes.titlesize': 10,
              'font.size': 10, # was 10
              'legend.fontsize': 8, # was 10
              'xtick.labelsize': 10,
              'ytick.labelsize': 10,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height],
              'lines.linewidth': 0.5,
              'font.family': 'serif',
              'grid.linestyle':':',
              'grid.linewidth' : 0.35,
              'axes.grid': False,
              'axes.grid.axis': 'both',
              'axes.grid.which': 'both',
              'axes.spines.bottom': True,
              'axes.spines.left': True,
              'axes.spines.right': True,
              'axes.spines.top': True,
              # 'xtick.minor.visible': True,
              # 'ytick.minor.visible': True,
              'xtick.bottom': True,
              'xtick.top': True,
              'xtick.color': 'black',
              'xtick.direction': 'out',
              'ytick.left': True,
              'ytick.right': True,
              'ytick.color': 'black',
              'ytick.direction': 'out',
    }

    rcParams.update(params)
    #pyplot.tight_layout()
##################################################################################################
def main():
    latexify(columns=2)
    ###  Fig 1 ###
    return

if __name__ == "__main__":
    main()

