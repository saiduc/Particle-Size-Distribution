from box import Box
import numpy as np
import matplotlib.pyplot as plt


def psi(x, R0):
    return x * (R0**2 - x**2)**(-0.5)


def plotHist(data, R0, nbins=10):
    # get histogram
    hist = plt.hist(data, nbins, align='mid', normed=False)
    plt.clf()

    # plot x and y from experiment
    x = hist[1][:-1]
    y = hist[0][:]
    plt.plot(x, y, marker="x", linestyle="")

    # plot x and y from theory
    x = np.linspace(0, R0, 1000)
    y = psi(x, R0)
    x = x[:-1]
    y = y[:-1]
    plt.plot(x, y)

    plt.show()


if __name__ == '__main__':
    box = Box(20)
    radius = 0.3
    box.populate(radius, 2500)

    box.addPlane(0, 0, 1, 10)

    box.calcCrossSections()

    crossSections = box.crossSections
    print(len(crossSections))
    centres = box.centres

    plotHist(crossSections, radius, 25)
