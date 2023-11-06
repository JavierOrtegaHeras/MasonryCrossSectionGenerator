''' Developed by J. Ortega
as part of the S-RAY Project, funded by the Fundación General CSIC´s ComFuturo programme, under the Marie Skłodowska-Curie grant agreement No. 101034263

Last changes made on September 11, 2023, in Madrid, Spain
'''

import ezdxf
import os
from section import *

if __name__ == '__main__':
    # divide cross-section of X,Y dimension into several areas to insert stones
    X = 0.6
    Y = 0.4
    K = 0.75  # minimum amount of stone allowed per area (to avoid much mortar in the cross-section)
    sides = 14  # sides of polygon of each stone (may be variable among stones or fixed)
    n = 3 # number of cross-sections to generate

    # create folder to save the cross-sections
    directory = 'sections' # name the folder where the dxf files will be creater
    parent_dir = 'output/' # the code will create the files in the output folder within the project
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    pathname = parent_dir + directory + '/'

    for j in range(0, n):
        crosssection = random.randint(1, 4)

        if crosssection != 1:
            StoneA, StoneB, StoneC, StoneD, StoneE, StoneF, LineA, LineB, LineC, LineD, LineE, LineF = GenerateCrossSect(X, Y, K, sides)

            # export to dxf so it can be exported to comsol
            doc = ezdxf.new("R2010", setup=True)
            msp = doc.modelspace()
            for i in range(0, len(StoneA)):
                msp.add_line(StoneA[i - 1], StoneA[i])
            for i in range(0, len(StoneB)):
                msp.add_line(StoneB[i - 1], StoneB[i])
            for i in range(0, len(StoneC)):
                msp.add_line(StoneC[i - 1], StoneC[i])
            for i in range(0, len(StoneD)):
                msp.add_line(StoneD[i - 1], StoneD[i])
            for i in range(0, len(StoneE)):
                msp.add_line(StoneE[i - 1], StoneE[i])
            for i in range(0, len(StoneF)):
                msp.add_line(StoneF[i - 1], StoneF[i])
            msp.add_line(LineA[0], LineA[1])
            if len(LineB) > 0: msp.add_line(LineB[0], LineB[1])
            msp.add_line(LineC[0], LineC[1])
            if len(LineD) > 0: msp.add_line(LineD[0], LineD[1])
            msp.add_line(LineE[0], LineE[1])
            msp.add_line(LineF[0], LineF[1])
            #doc.saveas('C:/Users/johe0/Desktop/sections/section' + str(j) + '.dxf')
            doc.saveas(pathname + 'section' + str(j) + '.dxf')

        else:
            StoneA, StoneB, StoneC, StoneD, StoneE, LineA, LineB, LineC, LineD, LineE, LineF = GenerateCrossSectTS(X, Y, K, sides)

            # export to dxf so it can be exported to comsol
            doc = ezdxf.new("R2010", setup=True)
            msp = doc.modelspace()
            for i in range(0, len(StoneA)):
                msp.add_line(StoneA[i - 1], StoneA[i])
            for i in range(0, len(StoneB)):
                msp.add_line(StoneB[i - 1], StoneB[i])
            for i in range(0, len(StoneC)):
                msp.add_line(StoneC[i - 1], StoneC[i])
            for i in range(0, len(StoneD)):
                msp.add_line(StoneD[i - 1], StoneD[i])
            for i in range(0, len(StoneE)):
                msp.add_line(StoneE[i - 1], StoneE[i])
            if len(LineA) > 0: msp.add_line(LineA[0], LineA[1])
            if len(LineB) > 0: msp.add_line(LineB[0], LineB[1])
            if len(LineC) > 0: msp.add_line(LineC[0], LineC[1])
            if len(LineD) > 0: msp.add_line(LineD[0], LineD[1])
            if len(LineE) > 0: msp.add_line(LineE[0], LineE[1])
            if len(LineF) > 0: msp.add_line(LineF[0], LineF[1])
            doc.saveas(pathname + 'section' + str(j) + '.dxf')
