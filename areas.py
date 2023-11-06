"""
Created on Tue Jun 20 16:51:14 2023

@author: johe0
"""
import random

def divideCrossSect(X=0.7, Y=0.5, a=2, b=3,
                    # c = 2, (in case we want to change the vertical division of the cross-section)
                    ):
    # #plot rectangle
    # Xrectangle=[0,X,X,0]
    # Yrectangle=[0,0,Y,Y]
    # plt.plot(Xrectangle,Yrectangle,marker="o")

    # divide for number of divisions a and b in X and c in Y
    Xdiv1 = random.randint(a, b)
    Xdiv2 = random.randint(a, b)
    # Ydiv=c

    # create
    X1limits = []
    Y1limits = []
    X2limits = []
    Y2limits = []

    # randomly divide upper row
    if Xdiv1 == 2:
        X1a = random.randint(3, 7)
        X2a = 10 - X1a
        X1a, X2a = X1a * X / 10, X2a * X / 10
        X1limits.extend([X1a, X2a])
        # randomly divide vertically
        Y1a = random.randint(2, 8) * Y / 10
        Y2a = random.randint(2, 8) * Y / 10
        Y1limits.extend([Y1a, Y2a])
    else:
        X1a = random.randint(2, 7)
        X2a = random.randint(2, 9 - X1a)
        X3a = 10 - X1a - X2a
        X1a, X2a, X3a = X1a * X / 10, X2a * X / 10, X3a * X / 10
        X1limits.extend([X1a, X2a, X3a])
        # randomly divide vertically
        Y1a = random.randint(2, 8) * Y / 10
        Y2a = random.randint(2, 8) * Y / 10
        Y3a = random.randint(2, 8) * Y / 10
        Y1limits.extend([Y1a, Y2a, Y3a])

    # randomly divide bottom row
    if Xdiv2 == 2:
        X1b = random.randint(3, 7)
        X2b = 10 - X1b
        X1b, X2b = X1b * X / 10, X2b * X / 10
        X2limits.extend([X1b, X2b])
        # obtain height
        if Xdiv1 == 2:
            if X1b < X1a:
                Y1b = Y - Y1a
                Y2b = Y - max(Y1a, Y2a)
            else:
                Y1b = Y - max(Y1a, Y2a)
                Y2b = Y - Y2a
        else:
            if X1b < X1a:
                Y1b = Y - Y1a
                Y2b = Y - max(Y1a, Y2a, Y3a)
            elif X1b < X1a + X2a:
                Y1b = Y - max(Y1a, Y2a)
                Y2b = Y - max(Y2a, Y3a)
            else:
                Y1b = Y - max(Y1a, Y2a, Y3a)
                Y2b = Y - Y3a
        Y2limits.extend([Y1b, Y2b])
    else:
        X1b = random.randint(2, 7)
        X2b = random.randint(2, 9 - X1b)
        X3b = 10 - X1b - X2b
        X1b, X2b, X3b = X1b * X / 10, X2b * X / 10, X3b * X / 10
        X2limits.extend([X1b, X2b, X3b])
        # obtain height
        if Xdiv1 == 2:
            if X1b < X1a:
                Y1b = Y - Y1a
                if X1b + X2b < X1a:
                    Y2b = Y - Y1a
                    Y3b = Y - max(Y1a, Y2a)
                else:
                    Y2b = Y - max(Y1a, Y2a)
                    Y3b = Y - Y2a
            else:
                Y1b = Y - max(Y1a, Y2a)
                Y2b = Y - Y2a
                Y3b = Y - Y2a
        else:
            if X1b < X1a:
                Y1b = Y - Y1a
                if X1b + X2b < X1a:
                    Y2b = Y - Y1a
                    Y3b = Y - max(Y1a, Y2a, Y3a)
                elif X1b + X2b < X1a + X2a:
                    Y2b = Y - max(Y1a, Y2a)
                    Y3b = Y - max(Y2a, Y3a)
                else:
                    Y2b = Y - max(Y1a, Y2a, Y3a)
                    Y3b = Y - Y3a
            elif X1b < X1a + X2a:
                Y1b = Y - max(Y1a, Y2a)
                if X1b + X2b < X1a + X2a:
                    Y2b = Y - Y2a
                    Y3b = Y - max(Y2a, Y3a)
                else:
                    Y2b = Y - max(Y2a, Y3a)
                    Y3b = Y - Y3a
            else:
                Y1b = Y - max(Y1a, Y2a, Y3a)
                Y2b = Y - Y3a
                Y3b = Y - Y3a
        Y2limits.extend([Y1b, Y2b, Y3b])

    return X1limits, Y1limits, X2limits, Y2limits


def divideCrossSectTS(X=0.7, Y=0.5):
    # decide position of Through Stone
    TS = random.randint(1, 3)
    print(TS)

    if TS == 1:
        # divide for number of divisions a and b in X and c in Y
        Xdiv1 = random.randint(1, 2)
        Xdiv2 = random.randint(1, 2)

        # create
        X1limits = []
        Y1limits = []
        X2limits = []
        Y2limits = []

        # randomly divide upper row
        if Xdiv1 == 1:
            X1a = random.randint(2, 4)
            X2a = 10 - X1a
            X1a, X2a = X1a * X / 10, X2a * X / 10
            X1limits.extend([X1a, X2a])
            # randomly divide vertically
            Y1a = Y
            Y2a = random.randint(2, 8) * Y / 10
            Y1limits.extend([Y1a, Y2a])
        else:
            X1a = random.randint(2, 4)
            X2a = random.randint(2, 9 - X1a)
            X3a = 10 - X1a - X2a
            X1a, X2a, X3a = X1a * X / 10, X2a * X / 10, X3a * X / 10
            X1limits.extend([X1a, X2a, X3a])
            # randomly divide vertically
            Y1a = Y
            Y2a = random.randint(2, 8) * Y / 10
            Y3a = random.randint(2, 8) * Y / 10
            Y1limits.extend([Y1a, Y2a, Y3a])

        # randomly divide bottom row
        if Xdiv2 == 1:
            X2b = X - X1a
            X2limits.extend([X2b])
            # obtain height
            if Xdiv1 == 1:
                Y2b = Y - Y2a
            else:
                if X2b < X2a:
                    Y2b = Y - Y2a
                else:
                    Y2b = Y - max(Y2a, Y3a)
            Y2limits.extend([Y2b])
        else:
            X2b = random.randint(2, 9 - (X1a * 10 / X))
            X2b = X2b * X / 10
            X3b = X - X1a - X2b
            X2limits.extend([X2b, X3b])
            # obtain height
            if Xdiv1 == 1:
                Y2b = Y - Y2a
                Y3b = Y - Y2a
            else:
                if X2b < X2a:
                    Y2b = Y - Y2a
                    Y3b = Y - max(Y2a, Y3a)
                else:
                    Y2b = Y - max(Y2a, Y3a)
                    Y3b = Y - Y3a
            Y2limits.extend([Y2b, Y3b])

    elif TS == 2:
        # create
        X1limits = []
        Y1limits = []
        X2limits = []
        Y2limits = []

        X2a = random.randint(2, 4)
        X1a = random.randint(2, 9 - X2a)
        X3a = 10 - X1a - X2a
        X1a, X2a, X3a = X1a * X / 10, X2a * X / 10, X3a * X / 10
        X1limits.extend([X1a, X2a, X3a])
        # randomly divide vertically
        Y1a = random.randint(2, 8) * Y / 10
        Y2a = Y
        Y3a = random.randint(2, 8) * Y / 10
        Y1limits.extend([Y1a, Y2a, Y3a])

        X1b = X1a
        X3b = X3a
        X2limits.extend([X1b, X3b])
        Y1b = Y - Y1a
        Y3b = Y - Y3a
        Y2limits.extend([Y1b, Y3b])

    else:
        # divide for number of divisions a and b in X and c in Y
        Xdiv1 = random.randint(1, 2)
        Xdiv2 = random.randint(1, 2)

        # create
        X1limits = []
        Y1limits = []
        X2limits = []
        Y2limits = []

        # randomly divide upper row
        if Xdiv1 == 1:
            X1a = random.randint(6, 8)
            X2a = 10 - X1a
            X1a, X2a = X1a * X / 10, X2a * X / 10
            X1limits.extend([X1a, X2a])
            # randomly divide vertically
            Y1a = random.randint(2, 8) * Y / 10
            Y2a = Y
            Y1limits.extend([Y1a, Y2a])
        else:
            X3a = random.randint(2, 4)
            X2a = random.randint(2, 9 - X3a)
            X1a = 10 - X3a - X2a
            X1a, X2a, X3a = X1a * X / 10, X2a * X / 10, X3a * X / 10
            X1limits.extend([X1a, X2a, X3a])
            # randomly divide vertically
            Y1a = random.randint(2, 8) * Y / 10
            Y2a = random.randint(2, 8) * Y / 10
            Y3a = Y
            Y1limits.extend([Y1a, Y2a, Y3a])

        # randomly divide bottom row
        if Xdiv2 == 1:
            if Xdiv1 == 1:
                X1b = X - X2a
                X2limits.extend([X1b])
                # obtain height
                if Xdiv1 == 1:
                    Y1b = Y - Y1a
                else:
                    if X1b < X1a:
                        Y1b = Y - Y1a
                    else:
                        Y1b = Y - max(Y1a, Y2a)
                Y2limits.extend([Y1b])
            else:
                X1b = X - X3a
                X2limits.extend([X1b])
                # obtain height
                if Xdiv1 == 1:
                    Y1b = Y - Y1a
                else:
                    if X1b < X1a:
                        Y1b = Y - Y1a
                    else:
                        Y1b = Y - max(Y1a, Y2a)
                Y2limits.extend([Y1b])
        else:
            if Xdiv1 == 1:
                X1b = random.randint(2, 9 - (X2a * 10 / X))
                X1b = X1b * X / 10
                X2b = X - X1b - X2a
                # obtain height
                Y1b = Y - Y1a
                Y2b = Y - Y1a
            else:
                X1b = random.randint(2, 9 - (X3a * 10 / X))
                X1b = X1b * X / 10
                X2b = X - X1b - X3a
                # obtain height
                if X1b < X1a:
                    Y1b = Y - Y1a
                    Y2b = Y - max(Y1a, Y2a)
                else:
                    Y1b = Y - max(Y1a, Y2a)
                    Y2b = Y - Y2a
            X2limits.extend([X1b, X2b])
            Y2limits.extend([Y1b, Y2b])

    return X1limits, Y1limits, X2limits, Y2limits