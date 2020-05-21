import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


class Box:
    """
    Box of spheres
    Takes input: boxLength
    """
    def __init__(self, boxLength):
        super(Box, self).__init__()
        self.boxLength = boxLength
        self.sphereRadius = 0
        self.N = 0
        self.coordinates = []

    def populate(self, radius, numberSpheres):

        self.sphereRadius = radius
        self.N = numberSpheres

        if self.boxLength < 2 * self.sphereRadius:
            print("box too small")
            return

        coordinate = np.array(
            [np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
             np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
             np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius)])

        spheres = [coordinate]

        while len(spheres) < self.N:
            coordinate = np.array(
                [np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
                 np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius),
                 np.random.uniform(self.sphereRadius, self.boxLength-self.sphereRadius)])

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
        plt.show()

    def addPlace(self):
        pass
