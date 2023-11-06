# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:54:06 2023

@author: Javier Ortega
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from areas import *

def first_non_consecutive(lst):
    i = 1
    while i < len(lst):
        if lst[i]-lst[i-1] != 1:
            return i,lst[i]
            break
        i += 1
    else:
        return 0,1


def randomStone(sides=12, A=0.35, B=0.25):
    # generate two lists of random X and Y coordinates
    Xcoords = random.sample(range(0, 100), sides)
    Ycoords = random.sample(range(0, 100), sides)

    # sort coordinates
    Xcoords.sort()
    Ycoords.sort()

    # randomly divide the interior points into two chains
    # X coords
    Xcoord1 = (Xcoords[1:-1])
    random.shuffle(Xcoord1)
    Xcoord1a = Xcoord1[0:int(sides / 2 - 1)]
    Xcoord1a.sort()
    Xcoord1a.insert(0, Xcoords[0])
    Xcoord1a.append(Xcoords[len(Xcoords) - 1])
    Xcoord1b = Xcoord1[int(sides / 2 - 1):sides - 2]
    Xcoord1b.sort()
    Xcoord1b.insert(0, Xcoords[0])
    Xcoord1b.append(Xcoords[len(Xcoords) - 1])
    # Y coords
    Ycoord1 = (Ycoords[1:-1])
    random.shuffle(Ycoord1)
    Ycoord1a = Ycoord1[0:int(sides / 2 - 1)]
    Ycoord1a.sort()
    Ycoord1a.insert(0, Ycoords[0])
    Ycoord1a.append(Ycoords[len(Ycoords) - 1])
    Ycoord1b = Ycoord1[int(sides / 2 - 1):sides - 2]
    Ycoord1b.sort()
    Ycoord1b.insert(0, Ycoords[0])
    Ycoord1b.append(Ycoords[len(Ycoords) - 1])

    # extract the vector components
    # X vectors
    Xvectors = []
    Xcoord1b.reverse()
    for i in range(1, len(Xcoord1a)):
        Xvectors.append(Xcoord1a[i - 1:i + 1])
        i = i + 1
    for i in range(1, len(Xcoord1b)):
        Xvectors.append(Xcoord1b[i - 1:i + 1])
        i = i + 1
    # Y vectors
    Yvectors = []
    Ycoord1b.reverse()
    for i in range(1, len(Ycoord1a)):
        Yvectors.append(Ycoord1a[i - 1:i + 1])
        i = i + 1
    for i in range(1, len(Ycoord1b)):
        Yvectors.append(Ycoord1b[i - 1:i + 1])
        i = i + 1

    # randomly pair up X- and Y-components and combine the into vectors [x1 y1] [x2 y2]
    random.shuffle(Yvectors)
    Ypaired = np.array(Yvectors)
    Xpaired = np.array(Xvectors)
    paired = np.stack((Xpaired, Ypaired), axis=2)

    # sort the vectors by angle
    angles = []
    lengths1 = []
    for i in range(0, len(paired)):
        angles.append(np.arctan2((paired[i][1][1] - paired[i][0][1]), (paired[i][1][0] - paired[i][0][0])))
        lengths1.append(
            np.sqrt(np.square(paired[i][1][1] - paired[i][0][1]) + np.square(paired[i][1][0] - paired[i][0][0])))
        i = i + 1

    lengths = [x for _, x in sorted(zip(angles, lengths1))]
    angles.sort()

    # form a polygon laying angles end-to-end
    Xpoints = []
    Xpoints.append(0)
    for i in range(0, len(angles)):
        Xpoints.append(Xpoints[i] + (lengths[i] * np.cos(angles[i])))
        i = i + 1

    Ypoints = []
    Ypoints.append(0)
    for i in range(0, len(angles)):
        Ypoints.append(Ypoints[i] + (lengths[i] * np.sin(angles[i])))
        i = i + 1

    # move polygon and scale them to min and max coordinates
    Xpoints = np.array([(i - (min(Xpoints))) * (A / 100) for i in Xpoints])
    Xpoints = Xpoints[:-1]  # to add duplicate point only after transformation of the stone
    Ypoints = np.array([(i - (min(Ypoints))) * (B / 100) for i in Ypoints])
    Ypoints = Ypoints[:-1]  # to add duplicate point only after transformation of the stone

    return Xpoints, Ypoints


def BotLefSt(Xpoints, Ypoints, sides, l, h):
    for i in range(0, sides):
        if Xpoints[i] < 0.015:
            # Xpoints[i]=0+random.randint(-50,50)/10000
            Xpoints[i] = 0

    for i in range(0, sides):
        if Ypoints[i] < 0.015:
            # Ypoints[i]=0+random.randint(-50,50)/10000
            Ypoints[i] = 0

    # add corner point
    d = np.sqrt(np.square(max(Xpoints)) + np.square(max(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(Xpoints[i]) + np.square(Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = 0
    Xpoints[closest_point - 1] = 0
    Xpoints[closest_point - 2] = 0
    Ypoints[closest_point] = 0
    Ypoints[closest_point + 1] = 0
    Ypoints[closest_point + 2] = 0

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def BotRigSt(Xpoints, Ypoints, sides, l, h):
    for i in range(0, sides):
        if Xpoints[i] > (l - 0.015):
            # Xpoints[i]=l+random.randint(-50,50)/10000
            Xpoints[i] = l

    for i in range(0, sides):
        if Ypoints[i] < 0.015:
            # Ypoints[i]=0+random.randint(-50,50)/10000
            Ypoints[i] = 0

    # add corner point
    d = np.sqrt(np.square(l - min(Xpoints)) + np.square(max(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(l - Xpoints[i]) + np.square(Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = l
    if closest_point + 1 < sides: Xpoints[closest_point + 1] = l
    if closest_point + 2 < sides: Xpoints[closest_point + 2] = l
    Ypoints[closest_point] = 0
    Ypoints[closest_point - 1] = 0
    Ypoints[closest_point - 2] = 0

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def BotSt(Xpoints, Ypoints, sides, l, h):
    bottompoints = []
    for i in range(0, sides):
        if Ypoints[i] < 0.025:
            # Ypoints[i]=0+random.randint(-50,50)/10000
            Ypoints[i] = 0
            bottompoints.append(i)

    if (Xpoints[min(bottompoints)] - Xpoints[min(bottompoints) - 1]) > 0.015:
        Ypoints[min(bottompoints) - 1] = 0

    if (Xpoints[max(bottompoints) + 1] - Xpoints[max(bottompoints)]) > 0.015:
        Ypoints[max(bottompoints) + 1] = 0

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def TopLefSt(Xpoints, Ypoints, sides, l, h):
    for i in range(0, sides):
        if Xpoints[i] < 0.015:
            # Xpoints[i]=0+random.randint(-50,50)/10000
            Xpoints[i] = 0

    for i in range(0, sides):
        if Ypoints[i] > (h - 0.015):
            # Ypoints[i]=h+random.randint(-50,50)/10000
            Ypoints[i] = h

    # add corner point
    d = np.sqrt(np.square(max(Xpoints)) + np.square(h - min(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(Xpoints[i]) + np.square(h - Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = 0
    Xpoints[closest_point + 1] = 0
    Xpoints[closest_point + 2] = 0
    Ypoints[closest_point] = h
    Ypoints[closest_point - 1] = h
    Ypoints[closest_point - 2] = h

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def TopRigSt(Xpoints, Ypoints, sides, l, h):
    for i in range(0, sides):
        if Xpoints[i] > (l - 0.015):
            # Xpoints[i]=l+random.randint(-50,50)/10000
            Xpoints[i] = l

    for i in range(0, sides):
        if Ypoints[i] > (h - 0.015):
            # Ypoints[i]=h+random.randint(-50,50)/10000
            Ypoints[i] = h

    # add corner point
    d = np.sqrt(np.square(l - min(Xpoints)) + np.square(h - min(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(l - Xpoints[i]) + np.square(h - Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = l
    Xpoints[closest_point - 1] = l
    Xpoints[closest_point - 2] = l
    Ypoints[closest_point] = h
    if (closest_point + 1) < (sides):
        Ypoints[closest_point + 1] = h
    else:
        Ypoints[0] = h
        Ypoints[1] = h
    if (closest_point + 2) < (sides):
        Ypoints[closest_point + 2] = h
    else:
        Ypoints[0] = h

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def TopSt(Xpoints, Ypoints, sides, l, h):
    toppoints = []
    for i in range(0, sides):
        if Ypoints[i] > (h - 0.025):
            Ypoints[i] = h
            toppoints.append(i)

    if len(toppoints) == 0:
        Ypoints[0] = h
        if (Xpoints[-1] - Xpoints[0]) > 0.015:
            Ypoints[-1] = h

        if (Xpoints[0] - Xpoints[1]) > 0.015:
            Ypoints[1] = h
    elif len(toppoints) == 1:
        Ypoints[0] = h
        if (Xpoints[-1] - Xpoints[0]) > 0.015:
            Ypoints[-1] = h

        if (Xpoints[0] - Xpoints[1]) > 0.015:
            Ypoints[1] = h
    elif len(toppoints) == 2:
        Ypoints[0] = h
        Ypoints[1] = h
        if (Xpoints[-1] - Xpoints[0]) > 0.015:
            Ypoints[-1] = h

        if (Xpoints[1] - Xpoints[2]) > 0.015:
            Ypoints[2] = h
    else:
        m, n = first_non_consecutive(toppoints)
        if (Xpoints[n - 1] - Xpoints[n]) > 0.015:
            Ypoints[n - 1] = h

        if (Xpoints[m - 1] - Xpoints[m]) > 0.015:
            Ypoints[m] = h

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def TS1(Xpoints, Ypoints, sides, l, h):
    for i in range(0, sides):
        if Xpoints[i] < 0.015:
            # Xpoints[i]=0+random.randint(-50,50)/10000
            Xpoints[i] = 0

    for i in range(0, sides):
        if Ypoints[i] > (h - 0.015):
            # Ypoints[i]=h+random.randint(-50,50)/10000
            Ypoints[i] = h

    for i in range(0, sides):
        if Ypoints[i] < 0.015:
            # Ypoints[i]=0+random.randint(-50,50)/10000
            Ypoints[i] = 0

    # add corner point
    d = np.sqrt(np.square(max(Xpoints)) + np.square(h - min(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(Xpoints[i]) + np.square(h - Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = 0
    Xpoints[closest_point + 1] = 0
    Xpoints[closest_point + 2] = 0
    Ypoints[closest_point] = h
    Ypoints[closest_point - 1] = h
    Ypoints[closest_point - 2] = h

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    # add corner point
    d = np.sqrt(np.square(max(Xpoints)) + np.square(max(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(Xpoints[i]) + np.square(Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = 0
    Xpoints[closest_point - 1] = 0
    Xpoints[closest_point - 2] = 0
    Ypoints[closest_point] = 0
    Ypoints[closest_point + 1] = 0
    Ypoints[closest_point + 2] = 0

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def TS2(Xpoints, Ypoints, sides, l, h):
    toppoints = []
    for i in range(0, sides):
        if Ypoints[i] > (h - 0.025):
            Ypoints[i] = h
            toppoints.append(i)

    if len(toppoints) == 0:
        Ypoints[0] = h
        if (Xpoints[-1] - Xpoints[0]) > 0.015:
            Ypoints[-1] = h

        if (Xpoints[0] - Xpoints[1]) > 0.015:
            Ypoints[1] = h
    elif len(toppoints) == 1:
        Ypoints[0] = h
        if (Xpoints[-1] - Xpoints[0]) > 0.015:
            Ypoints[-1] = h

        if (Xpoints[0] - Xpoints[1]) > 0.015:
            Ypoints[1] = h
    elif len(toppoints) == 2:
        Ypoints[0] = h
        Ypoints[1] = h
        if (Xpoints[-1] - Xpoints[0]) > 0.015:
            Ypoints[-1] = h

        if (Xpoints[1] - Xpoints[2]) > 0.015:
            Ypoints[2] = h
    else:
        m, n = first_non_consecutive(toppoints)
        if (Xpoints[n - 1] - Xpoints[n]) > 0.015:
            Ypoints[n - 1] = h

        if (Xpoints[m - 1] - Xpoints[m]) > 0.015:
            Ypoints[m] = h

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    bottompoints = []
    for i in range(0, sides):
        if Ypoints[i] < 0.025:
            # Ypoints[i]=0+random.randint(-50,50)/10000
            Ypoints[i] = 0
            bottompoints.append(i)

    if (Xpoints[min(bottompoints)] - Xpoints[min(bottompoints) - 1]) > 0.015:
        Ypoints[min(bottompoints) - 1] = 0

    if (Xpoints[max(bottompoints) + 1] - Xpoints[max(bottompoints)]) > 0.015:
        Ypoints[max(bottompoints) + 1] = 0

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints


def TS3(Xpoints, Ypoints, sides, l, h):
    for i in range(0, sides):
        if Xpoints[i] > (l - 0.015):
            # Xpoints[i]=l+random.randint(-50,50)/10000
            Xpoints[i] = l

    for i in range(0, sides):
        if Ypoints[i] > (h - 0.015):
            # Ypoints[i]=h+random.randint(-50,50)/10000
            Ypoints[i] = h

    # add corner point
    d = np.sqrt(np.square(l - min(Xpoints)) + np.square(h - min(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(l - Xpoints[i]) + np.square(h - Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = l
    Xpoints[closest_point - 1] = l
    Xpoints[closest_point - 2] = l
    Ypoints[closest_point] = h
    if (closest_point + 1) < (sides):
        Ypoints[closest_point + 1] = h
    else:
        Ypoints[0] = h
        Ypoints[1] = h
    if (closest_point + 2) < (sides):
        Ypoints[closest_point + 2] = h
    else:
        Ypoints[0] = h

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    for i in range(0, sides):
        if Xpoints[i] > (l - 0.015):
            # Xpoints[i]=l+random.randint(-50,50)/10000
            Xpoints[i] = l

    for i in range(0, sides):
        if Ypoints[i] < 0.015:
            # Ypoints[i]=0+random.randint(-50,50)/10000
            Ypoints[i] = 0

    # add corner point
    d = np.sqrt(np.square(l - min(Xpoints)) + np.square(max(Ypoints)))
    for i in range(0, sides):
        d1 = np.sqrt(np.square(l - Xpoints[i]) + np.square(Ypoints[i]))
        if d1 < d:
            d = d1
            closest_point = i

    Xpoints[closest_point] = l
    if closest_point + 1 < sides: Xpoints[closest_point + 1] = l
    if closest_point + 2 < sides: Xpoints[closest_point + 2] = l
    Ypoints[closest_point] = 0
    Ypoints[closest_point - 1] = 0
    Ypoints[closest_point - 2] = 0

    Xpoints = np.append(Xpoints, Xpoints[0])
    Ypoints = np.append(Ypoints, Ypoints[0])

    return Xpoints, Ypoints