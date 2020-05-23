import numpy as np
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib

font = {'family': 'normal',
        'weight': 'bold',
        'size': 18}

matplotlib.rc('font', **font)


class Box:
    """
    Box of spheres
    Takes input: boxLength
    """
    def __init__(self, boxLength):
        self.boxLength = boxLength

    def populate(self, r, numberSpheres, rand=0):

        radius = r + np.random.uniform(-rand, rand)

        self.N = numberSpheres

        if self.boxLength < 2 * radius:
            print("box too small")
            return

        coordinate = np.array(
            [np.random.uniform(radius, self.boxLength-radius),
             np.random.uniform(radius, self.boxLength-radius),
             np.random.uniform(radius, self.boxLength-radius),
             radius])

        spheres = [coordinate]

        count = 0
        while len(spheres) < self.N and count < 1000000:

            radius = r + np.random.uniform(-rand, rand)

            count += 1
            coordinate = np.array(
                [np.random.uniform(radius, self.boxLength-radius),
                 np.random.uniform(radius, self.boxLength-radius),
                 np.random.uniform(radius, self.boxLength-radius),
                 radius])

            check = 0
            for item in spheres:
                if np.sqrt((item[0]-coordinate[0])**2 +
                           (item[1]-coordinate[1])**2 +
                           (item[2]-coordinate[2])**2) > \
                           (item[3]+coordinate[3]):
                    check += 0
                else:
                    check += 1

            if check == 0:
                spheres.append(coordinate)

        print("placed", len(spheres), "balls")
        self.coordinates = spheres

    def placeSphere(self, x, y, z, r):
        if hasattr(self, "coordinates"):
            self.coordinates.append([x, y, z, r])
        else:
            self.coordinates = []
            self.coordinates.append([x, y, z, r])

    def plotBox(self):

        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for coordinate in self.coordinates:
            ax.scatter(coordinate[0], coordinate[1], coordinate[2], c='blue')

            (xs, ys, zs) = self.drawSphere(coordinate[0],
                                           coordinate[1],
                                           coordinate[2],
                                           coordinate[3])
            ax.plot_surface(xs, ys, zs)

        if hasattr(self, "plane"):
            ax.plot_surface(self.plane[0], self.plane[1], self.plane[2])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.tight_layout()
        # plt.savefig("./Figures/box3d.pdf")
        plt.show()

    def addPlane(self, A, B, C, D):
        self.planeCoeffs = [A, B, C, D]
        (x, y) = np.meshgrid(np.linspace(0, self.boxLength, 1000),
                             np.linspace(0, self.boxLength, 1000))

        z = (A*x + B*y - D)/(-C)
        self.plane = [x, y, z]

    def calcCrossSections(self):

        A = self.planeCoeffs[0]
        B = self.planeCoeffs[1]
        C = self.planeCoeffs[2]
        D = self.planeCoeffs[3]

        radii = []
        centres = []

        for coordinate in self.coordinates:
            x0 = coordinate[0]
            y0 = coordinate[1]
            z0 = coordinate[2]
            radius = coordinate[3]

            rho = (A*x0 + B*y0 + C*z0 - D)/np.sqrt(A**2 + B**2 + C**2)

            if abs(rho) < radius:
                r = np.sqrt(radius**2 - rho**2)
                radii.append(r)

                cx = x0 + rho * A/np.sqrt(A**2 + B**2 + C**2)
                cy = y0 + rho * B/np.sqrt(A**2 + B**2 + C**2)
                cz = z0 + rho * C/np.sqrt(A**2 + B**2 + C**2)

                centres.append([cx, cy, cz])

        self.centres = centres
        self.crossSections = radii

    def saveState(self):
        with open('population.dat', 'w') as f:
            csv.writer(f, delimiter=',').writerows(self.coordinates)

    def loadState(self, f):
        self.coordinates = np.loadtxt(f, dtype=float, delimiter=',')

    def drawSphere(self, xCenter, yCenter, zCenter, r):
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = np.cos(u)*np.sin(v)
        y = np.sin(u)*np.sin(v)
        z = np.cos(v)
        x = r*x + xCenter
        y = r*y + yCenter
        z = r*z + zCenter
        return (x, y, z)
