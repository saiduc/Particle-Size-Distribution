from box import Box
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

font = {'family': 'normal',
        'weight': 'bold',
        'size': 18}

matplotlib.rc('font', **font)

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

    if rand == 0:
        x = hist[1][:-1]
        y = hist[0][:]

        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(x, y, marker="x", linestyle="")

        plt.xlabel("Radius of Circle")
        plt.ylabel("Number of Circles")

        x = np.linspace(0, R0, 1000)
        y = psi(x, R0)
        x = x[:-1]
        y = y[:-1]

        plt.plot(x, y)

        # plt.title("750 Balls, 0.1 constant radius")
        # plt.tight_layout()
        # plt.savefig("./Figures/750_01.pdf")

    if rand != 0:
        x = hist[1][:-1]
        y = hist[0][:]
        y = y/np.sum(y)
        plt.plot(x, y, marker="x", linestyle="")

        plt.xlabel("Radius of Circle")
        plt.ylabel("Probability")

        R1 = R0 - rand
        R2 = R0 + rand
        x = np.linspace(0, R2, 1000)
        y = psi2(x, R1, R2)/2
        plt.plot(x, y)

        # plt.title("3500 Balls, 0.3 constant radius")
        # plt.tight_layout()
        # plt.savefig("./Figures/random_3500_03.pdf")

    plt.show()


if __name__ == '__main__':
    box = Box(20)
    radius = 0.1

    rand = 0.00
    box.populate(radius, 750, rand=rand)

    box.addPlane(0, 0, 1, 10)

    box.calcCrossSections()

    crossSections = box.crossSections
    print(len(crossSections))
    centres = box.centres

    plotHist(crossSections, radius, len(crossSections), rand=rand)
