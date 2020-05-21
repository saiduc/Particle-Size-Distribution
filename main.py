from box import Box


if __name__ == '__main__':
    box = Box(20)
    box.populate(0.7, 1500)

    box.addPlane(0, 0, 1, 10)

    box.calcCrossSections()

    box.plotBox()
