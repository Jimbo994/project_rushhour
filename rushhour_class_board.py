# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 21:40:57 2016

start of rush hour game

@author: Jim
"""
import math
import random
import rushhour_visualize
import pylab
import matplotlib, numpy

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
        
    def getNewPosition():
        raise NotImplementedError

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        #raise NotImplementedError
        
    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        checkX = pos.getX()
        checkY = pos.getY()
        
        if checkX < 0 or checkX > self.width:
            return False
        elif checkY < 0 or checkX > self.height:
            return False
        else:
            return True

def runSimulation(width, height):
        anim = rushhour_visualize.BoardVisualization(width, height)
        anim.done()

    
runSimulation(10,10)