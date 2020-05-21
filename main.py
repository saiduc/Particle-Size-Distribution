from box import Box
import numpy as np
import matplotlib.pyplot as plt


def psi(x, R0):
    return x * (R0**2 - x**2)**(0.5)


def plotHist(data, R0, nbins=10):
    hist = plt.hist(data, nbins)
    plt.clf()

    x = np.linspace(0, max(hist[1]), 1000)
    y = psi(x, R0)
    plt.plot(x, y)

    plt.show()


if __name__ == '__main__':
    box = Box(10)
    box.populate(0.5, 20)

    box.addPlane(0, 1, -1, 0)
    box.plotBox()

    box.calcCrossSections()

    crossSections = box.crossSections
    print(crossSections)
    centres = box.centres

    plotHist(crossSections, 0.7, 20)
