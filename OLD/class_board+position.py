# -*- coding: utf-8 -*-
# JIM

import math
import pylab
import matplotlib, numpy

class Position(object):
# location on 2D array board 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # get X & Y coordinates
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def isPositionOnBoard(self, pos):
        # check if position is on board. True = in room.
        checkX = pos.getX()
        checkY = pos.getY()
        
        if checkX < 0 or checkX > self.width:
            return False
        elif checkY < 0 or checkX > self.height:
            return False
        else:
            return True
