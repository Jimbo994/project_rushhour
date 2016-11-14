# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 21:40:57 2016

start of rush hour game

@author: Jim
"""
import math
# import random
import pylab
import matplotlib, numpy

class Position(object):
    """
    A Position represents a location on a two-dimensional board.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
>>    def getNewPosition(): <<

class Board(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def isPositionOnBoard(self, pos):
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
