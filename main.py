from box import Box
import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib
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
        plt.plot(x, y, marker="x", linestyle="", c="k")

        plt.xlabel("Radius of Circle")
        plt.ylabel("Number of Circles")

        x = np.linspace(0, R0, 1000)
        y = psi(x, R0)
        x = x[:-1]
        y = y[:-1]

        plt.plot(x, y, c="r", label="Theoretical Distribution")

        # plt.legend()
        # plt.tight_layout()
        # plt.savefig("./Figures/750_07_Noise_10.pdf")

    if rand != 0:
        x = hist[1][:-1]
        y = hist[0][:]
        y = y/np.sum(y)

        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.plot(x, y, marker="x", linestyle="", c="k")

        plt.xlabel("Radius of Circle")
        plt.ylabel("Probability")

        R1 = R0 - rand
        R2 = R0 + rand
        x = np.linspace(0, R2, 1000)
        y = psi2(x, R1, R2)/2
        plt.plot(x, y, c="r", label="Theoretical Distribution")

        # plt.legend()
        # plt.tight_layout()
        # plt.savefig("./Figures/750_07_random.pdf")

    plt.show()


def plotCircles():

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    circle1 = plt.Circle((2, 2), 1, color='black', fill=False)
    circle2 = plt.Circle((3, 6), 2, color='black', fill=False)
    circle3 = plt.Circle((7, 3), 0.3, color='black', fill=False)
    circle4 = plt.Circle((8, 8), 0.7, color='black', fill=False)
    circle5 = plt.Circle((5, 1.5), 0.5, color='black', fill=False)
    circle6 = plt.Circle((6.8, 5.3), 1.1, color='black', fill=False)
    circle7 = plt.Circle((8, 1), 0.8, color='black', fill=False)
    circle8 = plt.Circle((5.3, 8.9), 0.4, color='black', fill=False)

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    ax.add_artist(circle4)
    ax.add_artist(circle5)
    ax.add_artist(circle6)
    ax.add_artist(circle7)
    ax.add_artist(circle8)

    plt.xlim([0, 10])
    plt.ylim([0, 10])

    plt.xlabel("x")
    plt.ylabel("y")

    plt.tight_layout()
    plt.savefig("./Figures/circles.pdf")

    plt.show()


def randomiseCrossSection(crossSections, noise):
    tmp = []
    for i in crossSections:
        i += np.random.uniform(-noise, noise)
        tmp.append(i)
    return np.array(tmp)


if __name__ == '__main__':
# if True:
    box = Box(20)
    radius = 0.7

    rand = 0.00
    box.populate(radius, 750, rand=rand)

    box.addPlane(0, 0, 1, 10)

    box.calcCrossSections()

    crossSections = np.array(box.crossSections)
    print(len(crossSections))

    plotHist(crossSections, radius, int(len(crossSections)), rand=rand)
