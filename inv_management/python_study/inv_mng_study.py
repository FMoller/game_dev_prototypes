"""
Simple study about a inventory management system
"""

__version__ = "0.1"
__author__ = "Frederico Moeller"
__copyright__ = "Copyright 2021, Frederico Moeller"
__license__ = "MIT"


import numpy as np


class Inventory():
    """ Class that defines player's inventory """

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols
        self.inv = []
        self.stk = []
        self.area = np.zeros((rows,cols))

    def find_space(self,space):
        comparing = np.zeros(space)
        for i in range(self.rows-space[0]):
            for j in range(self.cols-space[1]):
                if False not in (self.area[i:i+space[0],j:j+space[1]] == comparing):
                    return [i,j]
        return [-1,-1]

    def add_object(self, obj):
        if obj.stackable:
            if obj.base_id in self.stk:
                

class Object():
    """ Simple object"""

    def __init__(self, name, space, stackable, weight, base_id, max_stack, stack=0):
        self.name = name
        self.space = space
        self.stackable = stackable
        self.weight = weight
        self.stack = stack
        self.max_stack = max_stack
        self.base_id = base_id
            



