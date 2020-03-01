import math


def firstrun():
    return "success"


def retarea(radius):
    area = radius*radius*math.pi
    area = round(area, 2)
    return area


def retlist(inplist):
    return inplist[0], inplist[-1]

