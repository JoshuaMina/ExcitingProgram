import numpy as np
import pygame
import math
import sys

Rows = 3
Columns = 3
sizeofsquare = 200
radiusofcircle = 60
offset = 55
circlelinewidth= 15
xlinewidth = 25
widthofscreen = Columns * sizeofsquare
heightofscreen = Rows * sizeofsquare
colorofline = (0,0,0)
backgroundcolour = (4,0,127)
colorofcircle= (255,255,0)
xcolor = (255,0,0)
player = 0
gameover = False
inmenu = True

def printingboard():
    flippedboard = np.flip(Board, 0)
    print(flippedboard)
    print("")