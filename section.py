"""
Created on Fri Jun 23 11:19:16 2023

@author: johe0
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import ezdxf
import os
from shapely.geometry import Polygon
from areas import *
from stones import *


def GenerateCrossSect(X=0.6, Y=0.4, K=0.75, sides=14):
    X1limits, Y1limits, X2limits, Y2limits = divideCrossSect(X, Y)

    print(X1limits, Y1limits, X2limits, Y2limits)  # coordinates of an ashlar cross section of randomn distribution

    # draw polygons
    fig = plt.figure()

    for i in range(0, len(X1limits)):
        l = X1limits[i]
        h = Y1limits[i]
        AreaTot = X1limits[i] * Y1limits[i]
        Xpoints, Ypoints = randomStone(sides, l, h)
        coords = list(zip(Xpoints, Ypoints))
        AreaSt = Polygon(coords).area
        while AreaSt < K * AreaTot:
            Xpoints, Ypoints = randomStone(sides, l, h)
            coords = list(zip(Xpoints, Ypoints))
            AreaSt = Polygon(coords).area
            # print("Iter")
        Ypoints = Ypoints + (Y - Y1limits[i])
        if i == 0:
            Xpoints, Ypoints = TopLefSt(Xpoints, Ypoints, sides, l, Y)
            leftrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == 0]
            XPointA, YPointA = (0, min(leftrow))
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointB, YPointB = (max(toprow), Y)
            StoneA = []
            for j in range(0, sides):
                StoneA.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X1limits) == 2:
            Xpoints = Xpoints + X1limits[i - 1]
            Xpoints, Ypoints = TopRigSt(Xpoints, Ypoints, sides, X, Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointC, YPointC = (min(toprow), Y)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointD, YPointD = (X, min(rightrow))
            plt.plot([XPointB, XPointC], [YPointB, YPointC])
            LineA = []
            LineB = []
            LineA.append((XPointB, YPointB))
            LineA.append((XPointC, YPointC))
            StoneB = []
            StoneC = []
            for j in range(0, sides):
                StoneB.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X1limits) == 3:
            Xpoints = Xpoints + X1limits[i - 1]
            Xpoints, Ypoints = TopSt(Xpoints, Ypoints, sides, l + X1limits[0], Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointC, YPointC = (min(toprow), Y)
            XPointD, YPointD = (max(toprow), Y)
            plt.plot([XPointB, XPointC], [YPointB, YPointC])
            LineA = []
            LineA.append((XPointB, YPointB))
            LineA.append((XPointC, YPointC))
            StoneB = []
            for j in range(0, sides):
                StoneB.append((Xpoints[j], Ypoints[j]))
            # return StoneB
        else:
            Xpoints = Xpoints + X1limits[i - 1] + X1limits[i - 2]
            Xpoints, Ypoints = TopRigSt(Xpoints, Ypoints, sides, X, Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointE, YPointE = (min(toprow), Y)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointF, YPointF = (X, min(rightrow))
            plt.plot([XPointD, XPointE], [YPointD, YPointE])
            LineB = []
            LineB.append((XPointD, YPointD))
            LineB.append((XPointE, YPointE))
            StoneC = []
            for j in range(0, sides):
                StoneC.append((Xpoints[j], Ypoints[j]))
        plt.plot(Xpoints, Ypoints)
        # ax1.plot(Xpoints,Ypoints,marker='o')

    for i in range(0, len(X2limits)):
        l = X2limits[i]
        h = Y2limits[i]
        AreaTot = X2limits[i] * Y2limits[i]
        Xpoints, Ypoints = randomStone(sides, l, h)
        coords = list(zip(Xpoints, Ypoints))
        AreaSt = Polygon(coords).area
        while AreaSt < K * AreaTot:
            Xpoints, Ypoints = randomStone(sides, l, h)
            coords = list(zip(Xpoints, Ypoints))
            AreaSt = Polygon(coords).area
        if i == 0:
            Xpoints, Ypoints = BotLefSt(Xpoints, Ypoints, sides, l, h)
            leftrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == 0]
            XPointL, YPointL = (0, max(leftrow))
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointK, YPointK = (max(bottomrow), 0)
            plt.plot([XPointL, XPointA], [YPointL, YPointA])
            LineF = []
            LineF.append((XPointL, YPointL))
            LineF.append((XPointA, YPointA))
            StoneD = []
            for j in range(0, sides):
                StoneD.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X2limits) == 2:
            Xpoints = Xpoints + X2limits[i - 1]
            Xpoints, Ypoints = BotRigSt(Xpoints, Ypoints, sides, X, h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointJ, YPointJ = (min(bottomrow), 0)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointI, YPointI = (X, max(rightrow))
            plt.plot([XPointJ, XPointK], [YPointJ, YPointK])
            LineE = []
            LineE.append((XPointJ, YPointJ))
            LineE.append((XPointK, YPointK))
            LineC = []
            LineD = []
            if len(X1limits) == 2:
                plt.plot([XPointD, XPointI], [YPointD, YPointI])
                LineC.append((XPointD, YPointD))
                LineC.append((XPointI, YPointI))
            else:
                plt.plot([XPointF, XPointI], [YPointF, YPointI])
                LineC.append((XPointF, YPointF))
                LineC.append((XPointI, YPointI))
            StoneE = []
            StoneF = []
            for j in range(0, sides):
                StoneE.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X2limits) == 3:
            Xpoints = Xpoints + X2limits[0]
            Xpoints, Ypoints = BotSt(Xpoints, Ypoints, sides, l + X2limits[0], h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointJ, YPointJ = (min(bottomrow), 0)
            XPointI, YPointI = (max(bottomrow), 0)
            plt.plot([XPointJ, XPointK], [YPointJ, YPointK])
            LineE = []
            LineE.append((XPointJ, YPointJ))
            LineE.append((XPointK, YPointK))
            StoneE = []
            for j in range(0, sides):
                StoneE.append((Xpoints[j], Ypoints[j]))
        else:
            Xpoints = Xpoints + X2limits[i - 1] + X2limits[i - 2]
            Xpoints, Ypoints = BotRigSt(Xpoints, Ypoints, sides, X, h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointH, YPointH = (min(bottomrow), 0)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointG, YPointG = (X, max(rightrow))
            plt.plot([XPointH, XPointI], [YPointH, YPointI])
            LineD = []
            LineD.append((XPointH, YPointH))
            LineD.append((XPointI, YPointI))
            LineC = []
            if len(X1limits) == 2:
                plt.plot([XPointD, XPointG], [YPointD, YPointG])
                LineC.append((XPointD, YPointD))
                LineC.append((XPointG, YPointG))
            else:
                plt.plot([XPointF, XPointG], [YPointF, YPointG])
                LineC.append((XPointF, YPointF))
                LineC.append((XPointG, YPointG))
            StoneF = []
            for j in range(0, sides):
                StoneF.append((Xpoints[j], Ypoints[j]))
        plt.plot(Xpoints, Ypoints)

    plt.show()

    return StoneA, StoneB, StoneC, StoneD, StoneE, StoneF, LineA, LineB, LineC, LineD, LineE, LineF


def GenerateCrossSectTS(X=0.6, Y=0.4, K=0.75, sides=14):
    X1limits, Y1limits, X2limits, Y2limits = divideCrossSectTS(X, Y)

    print(X1limits, Y1limits, X2limits, Y2limits)  # coordinates of an ashlar cross section of randomn distribution

    # draw polygons
    fig = plt.figure()

    for i in range(0, len(X1limits)):
        l = X1limits[i]
        h = Y1limits[i]
        AreaTot = X1limits[i] * Y1limits[i]
        Xpoints, Ypoints = randomStone(sides, l, h)
        coords = list(zip(Xpoints, Ypoints))
        AreaSt = Polygon(coords).area
        while AreaSt < K * AreaTot:
            Xpoints, Ypoints = randomStone(sides, l, h)
            coords = list(zip(Xpoints, Ypoints))
            AreaSt = Polygon(coords).area
            # print("Iter")
        Ypoints = Ypoints + (Y - Y1limits[i])
        if i == 0 and Y1limits[0] == Y:
            Xpoints, Ypoints = TS1(Xpoints, Ypoints, sides, l, Y)
            # leftrow=[Ypoints[j] for j in range(0,sides) if Xpoints[j]==0]
            # XPointA,YPointA=(0,min(leftrow))
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointB, YPointB = (max(toprow), Y)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointK, YPointK = (max(bottomrow), 0)
            StoneA = []
            LineF = []
            for j in range(0, sides):
                StoneA.append((Xpoints[j], Ypoints[j]))
        elif i == 0:
            Xpoints, Ypoints = TopLefSt(Xpoints, Ypoints, sides, l, Y)
            leftrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == 0]
            XPointA, YPointA = (0, min(leftrow))
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointB, YPointB = (max(toprow), Y)
            StoneA = []
            for j in range(0, sides):
                StoneA.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X1limits) == 2 and Y1limits[1] == Y:
            Xpoints = Xpoints + X1limits[i - 1]
            Xpoints, Ypoints = TS3(Xpoints, Ypoints, sides, X, Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointE, YPointE = (min(toprow), Y)
            # rightrow=[Ypoints[j] for j in range(0,sides) if Xpoints[j]==X]
            # XPointD,YPointD=(X,min(rightrow))
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointH, YPointH = (min(bottomrow), 0)
            plt.plot([XPointB, XPointE], [YPointB, YPointE])
            LineA = []
            LineB = []
            LineC = []
            LineA.append((XPointB, YPointB))
            LineA.append((XPointE, YPointE))
            StoneB = []
            StoneC = []
            StoneD = []
            for j in range(0, sides):
                StoneC.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X1limits) == 2:
            Xpoints = Xpoints + X1limits[i - 1]
            Xpoints, Ypoints = TopRigSt(Xpoints, Ypoints, sides, X, Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointE, YPointE = (min(toprow), Y)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointF, YPointF = (X, min(rightrow))
            plt.plot([XPointB, XPointE], [YPointB, YPointE])
            LineA = []
            LineB = []
            LineF = []
            LineA.append((XPointB, YPointB))
            LineA.append((XPointE, YPointE))
            StoneB = []
            StoneC = []
            for j in range(0, sides):
                StoneB.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X1limits) == 3 and Y1limits[1] == Y:
            Xpoints = Xpoints + X1limits[i - 1]
            Xpoints, Ypoints = TS2(Xpoints, Ypoints, sides, l + X1limits[0], Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointC, YPointC = (min(toprow), Y)
            XPointD, YPointD = (max(toprow), Y)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointI, YPointI = (max(bottomrow), 0)
            XPointJ, YPointJ = (min(bottomrow), 0)
            plt.plot([XPointB, XPointC], [YPointB, YPointC])
            LineA = []
            LineA.append((XPointB, YPointB))
            LineA.append((XPointC, YPointC))
            StoneB = []
            for j in range(0, sides):
                StoneB.append((Xpoints[j], Ypoints[j]))
            # return StoneB
        elif i == 1 and len(X1limits) == 3:
            Xpoints = Xpoints + X1limits[i - 1]
            Xpoints, Ypoints = TopSt(Xpoints, Ypoints, sides, l + X1limits[0], Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointC, YPointC = (min(toprow), Y)
            XPointD, YPointD = (max(toprow), Y)
            plt.plot([XPointB, XPointC], [YPointB, YPointC])
            LineA = []
            LineA.append((XPointB, YPointB))
            LineA.append((XPointC, YPointC))
            StoneB = []
            for j in range(0, sides):
                StoneB.append((Xpoints[j], Ypoints[j]))
            # return StoneB
        elif i == 2 and Y1limits[2] == Y:
            Xpoints = Xpoints + X1limits[i - 1] + X1limits[i - 2]
            Xpoints, Ypoints = TS3(Xpoints, Ypoints, sides, X, Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointE, YPointE = (min(toprow), Y)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointH, YPointH = (min(bottomrow), 0)
            plt.plot([XPointD, XPointE], [YPointD, YPointE])
            LineB = []
            LineC = []
            LineB.append((XPointD, YPointD))
            LineB.append((XPointE, YPointE))
            StoneC = []
            StoneD = []
            for j in range(0, sides):
                StoneC.append((Xpoints[j], Ypoints[j]))
        else:
            Xpoints = Xpoints + X1limits[i - 1] + X1limits[i - 2]
            Xpoints, Ypoints = TopRigSt(Xpoints, Ypoints, sides, X, Y)
            toprow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == Y]
            XPointE, YPointE = (min(toprow), Y)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointF, YPointF = (X, min(rightrow))
            plt.plot([XPointD, XPointE], [YPointD, YPointE])
            LineB = []
            LineB.append((XPointD, YPointD))
            LineB.append((XPointE, YPointE))
            StoneC = []
            for j in range(0, sides):
                StoneC.append((Xpoints[j], Ypoints[j]))
        plt.plot(Xpoints, Ypoints)
        # ax1.plot(Xpoints,Ypoints,marker='o')

    for i in range(0, len(X2limits)):
        l = X2limits[i]
        h = Y2limits[i]
        AreaTot = X2limits[i] * Y2limits[i]
        Xpoints, Ypoints = randomStone(sides, l, h)
        coords = list(zip(Xpoints, Ypoints))
        AreaSt = Polygon(coords).area
        while AreaSt < K * AreaTot:
            Xpoints, Ypoints = randomStone(sides, l, h)
            coords = list(zip(Xpoints, Ypoints))
            AreaSt = Polygon(coords).area
        if i == 0 and len(X2limits) == 1 and Y1limits[0] == Y:
            Xpoints = Xpoints + X1limits[0]
            Xpoints, Ypoints = BotRigSt(Xpoints, Ypoints, sides, X, h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointH, YPointH = (min(bottomrow), 0)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointG, YPointG = (X, max(rightrow))
            plt.plot([XPointF, XPointG], [YPointF, YPointG])
            plt.plot([XPointH, XPointK], [YPointH, YPointK])
            LineC = []
            LineC.append((XPointF, YPointF))
            LineC.append((XPointG, YPointG))
            LineD = []
            LineE = []
            LineE.append((XPointH, YPointH))
            LineE.append((XPointK, YPointK))
            StoneD = []
            StoneE = []
            for j in range(0, sides):
                StoneD.append((Xpoints[j], Ypoints[j]))
        elif i == 0 and len(X2limits) == 1:
            Xpoints, Ypoints = BotLefSt(Xpoints, Ypoints, sides, l, h)
            leftrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == 0]
            XPointL, YPointL = (0, max(leftrow))
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointK, YPointK = (max(bottomrow), 0)
            plt.plot([XPointH, XPointK], [YPointH, YPointK])
            LineD = []
            LineE = []
            LineD.append((XPointH, YPointH))
            LineD.append((XPointK, YPointK))
            plt.plot([XPointL, XPointA], [YPointL, YPointA])
            LineF = []
            LineF.append((XPointL, YPointL))
            LineF.append((XPointA, YPointA))
            StoneD = []
            StoneE = []
            for j in range(0, sides):
                StoneE.append((Xpoints[j], Ypoints[j]))
        elif i == 0 and len(X2limits) == 2 and Y1limits[0] == Y:
            Xpoints = Xpoints + X1limits[0]
            Xpoints, Ypoints = BotSt(Xpoints, Ypoints, sides, X, h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointI, YPointI = (max(bottomrow), 0)
            XPointJ, YPointJ = (min(bottomrow), 0)
            plt.plot([XPointJ, XPointK], [YPointJ, YPointK])
            LineE = []
            LineE.append((XPointJ, YPointJ))
            LineE.append((XPointK, YPointK))
            StoneE = []
            for j in range(0, sides):
                StoneE.append((Xpoints[j], Ypoints[j]))
        elif i == 0 and len(X2limits) == 2 and len(X1limits) == 2 and Y1limits[1] == Y:
            Xpoints, Ypoints = BotLefSt(Xpoints, Ypoints, sides, X, h)
            leftrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == 0]
            XPointL, YPointL = (0, max(leftrow))
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointK, YPointK = (max(bottomrow), 0)
            plt.plot([XPointL, XPointA], [YPointL, YPointA])
            LineF = []
            LineF.append((XPointL, YPointL))
            LineF.append((XPointA, YPointA))
            StoneE = []
            for j in range(0, sides):
                StoneE.append((Xpoints[j], Ypoints[j]))
        elif i == 0 and len(X2limits) == 2 and Y1limits[1] == Y:
            Xpoints, Ypoints = BotLefSt(Xpoints, Ypoints, sides, X, h)
            leftrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == 0]
            XPointL, YPointL = (0, max(leftrow))
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointK, YPointK = (max(bottomrow), 0)
            plt.plot([XPointL, XPointA], [YPointL, YPointA])
            LineF = []
            LineF.append((XPointL, YPointL))
            LineF.append((XPointA, YPointA))
            plt.plot([XPointJ, XPointK], [YPointJ, YPointK])
            LineE = []
            LineE.append((XPointJ, YPointJ))
            LineE.append((XPointK, YPointK))
            StoneE = []
            for j in range(0, sides):
                StoneE.append((Xpoints[j], Ypoints[j]))
        elif i == 0 and len(X2limits) == 2:
            Xpoints, Ypoints = BotLefSt(Xpoints, Ypoints, sides, X, h)
            leftrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == 0]
            XPointL, YPointL = (0, max(leftrow))
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointK, YPointK = (max(bottomrow), 0)
            plt.plot([XPointL, XPointA], [YPointL, YPointA])
            LineF = []
            LineF.append((XPointL, YPointL))
            LineF.append((XPointA, YPointA))
            StoneE = []
            for j in range(0, sides):
                StoneE.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X2limits) == 2 and Y1limits[0] == Y:
            Xpoints = Xpoints + X1limits[0] + X2limits[0]
            Xpoints, Ypoints = BotRigSt(Xpoints, Ypoints, sides, X, h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointH, YPointH = (min(bottomrow), 0)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointG, YPointG = (X, max(rightrow))
            plt.plot([XPointF, XPointG], [YPointF, YPointG])
            LineC = []
            LineC.append((XPointF, YPointF))
            LineC.append((XPointG, YPointG))
            LineD = []
            plt.plot([XPointH, XPointI], [YPointH, YPointI])
            LineD.append((XPointH, YPointH))
            LineD.append((XPointI, YPointI))
            StoneD = []
            for j in range(0, sides):
                StoneD.append((Xpoints[j], Ypoints[j]))
        elif i == 1 and len(X2limits) == 2 and len(X1limits) == 3 and Y1limits[1] == Y:
            Xpoints = Xpoints + X1limits[1] + X2limits[0]
            Xpoints, Ypoints = BotRigSt(Xpoints, Ypoints, sides, X, h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointH, YPointH = (min(bottomrow), 0)
            rightrow = [Ypoints[j] for j in range(0, sides) if Xpoints[j] == X]
            XPointG, YPointG = (X, max(rightrow))
            plt.plot([XPointF, XPointG], [YPointF, YPointG])
            LineC = []
            LineC.append((XPointF, YPointF))
            LineC.append((XPointG, YPointG))
            plt.plot([XPointH, XPointI], [YPointH, YPointI])
            LineD = []
            LineD.append((XPointH, YPointH))
            LineD.append((XPointI, YPointI))
            StoneD = []
            for j in range(0, sides):
                StoneD.append((Xpoints[j], Ypoints[j]))
        else:
            Xpoints = Xpoints + X2limits[0]
            Xpoints, Ypoints = BotSt(Xpoints, Ypoints, sides, X, h)
            bottomrow = [Xpoints[j] for j in range(0, sides) if Ypoints[j] == 0]
            XPointI, YPointI = (max(bottomrow), 0)
            XPointJ, YPointJ = (min(bottomrow), 0)
            plt.plot([XPointH, XPointI], [YPointH, YPointI])
            LineD = []
            LineD.append((XPointH, YPointH))
            LineD.append((XPointI, YPointI))
            plt.plot([XPointJ, XPointK], [YPointJ, YPointK])
            LineE = []
            LineE.append((XPointJ, YPointJ))
            LineE.append((XPointK, YPointK))
            StoneD = []
            for j in range(0, sides):
                StoneD.append((Xpoints[j], Ypoints[j]))
        plt.plot(Xpoints, Ypoints)

    plt.show()

    return StoneA, StoneB, StoneC, StoneD, StoneE, LineA, LineB, LineC, LineD, LineE, LineF
