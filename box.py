import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def normalise(array):
    tmp = 0
    for i in array:
        tmp += i**2
    return np.sqrt(tmp)


def populateBox(boxLength, sphereRadius, N):

    if boxLength < 2*sphereRadius:
        print("Box too small")
        return

    coordinate = np.array(
        [np.random.uniform(sphereRadius, boxLength-sphereRadius),
         np.random.uniform(sphereRadius, boxLength-sphereRadius),
         np.random.uniform(sphereRadius, boxLength-sphereRadius)])

    spheres = [coordinate]

    while len(spheres) < N:
        coordinate = np.array(
            [np.random.uniform(sphereRadius, boxLength-sphereRadius),
             np.random.uniform(sphereRadius, boxLength-sphereRadius),
             np.random.uniform(sphereRadius, boxLength-sphereRadius)])

        appended = False
        for item in spheres:
            if abs(item[0]-coordinate[0]) > sphereRadius*2 and abs(item[1]-coordinate[1]) > sphereRadius*2 and abs(item[2]-coordinate[2]) > sphereRadius*2 and appended == False:
                spheres.append(coordinate)
                appended = True
                break

    return spheres


def plotBox(box):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for coordinate in box:
        ax.scatter(coordinate[0], coordinate[1], coordinate[2], color='blue')
    plt.show()


if __name__ == '__main__':
    box = populateBox(20, 0.7, 1500)
    plotBox(box)
