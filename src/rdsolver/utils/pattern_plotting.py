import matplotlib.pyplot as plt

def pattern_plot(conc):
    """
    Plotting the evolution of the concentration in time.
    """

    plt.ion()
    plt.clf()
    plt.imshow(conc, cmap="inferno", vmin=0, vmax=1)
    plt.tight_layout()
    plt.draw()
    plt.pause(0.01)
    plt.show(block=False)
