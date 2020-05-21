import numpy as np


def normalise(array):
    tmp = 0
    for i in array:
        tmp += i**2
    return np.sqrt(tmp)


boxLength = 20
sphereRadius = 0.7

coordinate = np.array(
    [np.random.uniform(sphereRadius, boxLength-sphereRadius),
     np.random.uniform(sphereRadius, boxLength-sphereRadius),
     np.random.uniform(sphereRadius, boxLength-sphereRadius)])

spheres = [coordinate]

# while len(spheres) < 1856:
while len(spheres) < 10:
    coordinate = np.array(
        [np.random.uniform(sphereRadius, boxLength-sphereRadius),
         np.random.uniform(sphereRadius, boxLength-sphereRadius),
         np.random.uniform(sphereRadius, boxLength-sphereRadius)])

    if any([abs(item[0]-coordinate[0]) > sphereRadius*2 and abs(item[1]-coordinate[1]) > sphereRadius*2 and abs(item[2]-coordinate[2]) > sphereRadius*2] for item in spheres):
        spheres.append(coordinate)
