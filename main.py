from box import Box
import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy.integrate import trapz
import math
warnings.filterwarnings("ignore")


def psi(x, R0):
    return x * (R0**2 - x**2)**(-0.5)


def psi2(x, R1, R2):
    a = x * np.log(np.sqrt(R2**2 - x**2 + 0j) + R2)
    b = x * np.log(np.sqrt(R1**2 - x**2 + 0j) + R1)
    return np.real(a - b)


def plotHist(data, R0, nbins=10, rand=0):
    # get histogram
    hist = plt.hist(data, nbins, align='mid')
    plt.clf()

    # plot x and y from experiment
    x = hist[1][:-1]
    y = hist[0][:]
    y = y/np.sum(y)
    plt.plot(x, y, marker="x", linestyle="")

    # plot x and y from theory
    if rand == 0:
        x = np.linspace(0, R0, 1000)
        y = psi(x, R0)
        x = x[:-1]
        y = y[:-1]
        plt.plot(x, y)

    if rand != 0:
        R1 = R0 - rand
        R2 = R0 + rand
        x = np.linspace(0, R2, 1000)
        y = psi2(x, R1, R2)/2
        plt.plot(x, y)

    plt.show()


if __name__ == '__main__':
    box = Box(20)
    radius = 0.3
    box.populate(radius, 2500, rand=0.05)

    box.addPlane(0, 0, 1, 10)

    box.calcCrossSections()

    crossSections = box.crossSections
    print(len(crossSections))
    centres = box.centres

    plotHist(crossSections, radius, 25, rand=0.05)
