from box import Box
import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy.integrate import trapz
warnings.filterwarnings("ignore")


def psi(x, R0):
    return x * (R0**2 - x**2)**(-0.5)


# def psi2(x, R1, R2):
#     a = x * np.log(np.sqrt(R2**2 - x**2) + R2)
#     b = x * np.log(np.sqrt(R1**2 - x**2) + R1)
#     return a - b

# def psi2(x, R1, R2):
#     items = []
#     deltaR = 0.01
#     N = int((R2 - R1)/deltaR)
#     for n in range(int(R1/deltaR), int(R2/deltaR)):
#         items.append(x/np.sqrt(n**2 * deltaR**2 - x**2))

#     return np.sum(items)

# def func(R, x):
#     return x * np.sqrt(R**2 - x**2)


# def psi2(x, R1, R2):
#     R = np.linspace(R1, R2, 1000)
#     y = func(R, x)
#     i = trapz(y, R, dx=0.01)
#     return i

# def Amn(n, m, dR):
#     if n > m:
#         return dR * m / np.sqrt(n**2 - m**2)
#     else:
#         return 0


# def psi2(m, R1, R2, dR):
#     tmp = 0
#     N = int((R2-R1)/dR)
#     for n in range(N):
#         tmp += Amn(n, m, dR)
#     return tmp


def plotHist(data, R0, nbins=10, rand=0):
    # get histogram
    hist = plt.hist(data, nbins, align='mid')
    plt.clf()

    # plot x and y from experiment
    x = hist[1][:-1]
    y = hist[0][:]
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
        y = []
        for i in x:
            y.append(psi2(i, R1, R2, 0.1))
        
        x = x[:-30]
        y = y[:-30]
        plt.plot(x, y)

    plt.show()


def print_radii(box):
    for i in box.coordinates:
        print(i[3])


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
