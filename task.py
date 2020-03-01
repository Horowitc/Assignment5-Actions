import math


def firstrun():
    return "success"


def retarea(radius):
    area = radius*radius*math.pi
    area = round(area, 2)
    return area


def retlist(inplist):
    return inplist[0], inplist[-1]


def leapyear(date):
    year = date[2]
    if date[0] <= 2:
        year -= 1
    return int(year / 4 - year / 100 + year / 400)


def retdate(date1, date2):
    daysinmon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
    num1 = date1[2]*365 + date1[1]
    for i in range(0, date1[0] - 1):
        num1 += daysinmon[i]
    num1 += leapyear(date1)

    num2 = date2[2] * 365 + date2[1]
    for i in range(0, date2[0] - 1):
        num2 += daysinmon[i]
    num2 += leapyear(date2)

    return num2 - num1
