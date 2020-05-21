import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


class Box:
    """
    Box of spheres
    Takes input: boxLength
    """
    def __init__(self, boxLength):
        self.boxLength = boxLength

    def populate(self, radius, numberSpheres):

        self.sphereRadius = radius
        self.N = numberSpheres

        if self.boxLength < 2 * self.sphereRadius:
            print("box too small")
            return

        coordinate = np.array(
            [np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
             np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
             np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
             radius])

        spheres = [coordinate]

        while len(spheres) < self.N:
            coordinate = np.array(
                [np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
                 np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
                 np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
                 radius])

            appended = False
            for item in spheres:
                if abs(item[0]-coordinate[0]) > self.sphereRadius*2 and \
                   abs(item[1]-coordinate[1]) > self.sphereRadius*2 and \
                   abs(item[2]-coordinate[2]) > self.sphereRadius*2 and \
                   appended is False:
                    spheres.append(coordinate)
                    appended = True
                    break

        self.coordinates = spheres

    def plotBox(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for coordinate in self.coordinates:
            ax.scatter(coordinate[0], coordinate[1], coordinate[2], c='blue')

        if hasattr(self, "plane"):
            ax.plot_surface(self.plane[0], self.plane[1], self.plane[2])
        plt.show()

    def addPlane(self, A, B, C, D):
        self.planeCoeffs = [A, B, C, D]
        (x, y) = np.meshgrid(np.linspace(0, 20, 1000),
                             np.linspace(0, 20, 1000))

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

            if -radius < rho < radius:
                r = np.sqrt(radius**2 - rho**2)
                radii.append(r)

                cx = x0 + rho * A/np.sqrt(A**2 + B**2 + C**2)
                cy = y0 + rho * B/np.sqrt(A**2 + B**2 + C**2)
                cz = z0 + rho * C/np.sqrt(A**2 + B**2 + C**2)

                centres.append([cx, cy, cz])

        self.centres = centres
        self.crossSections = radii
