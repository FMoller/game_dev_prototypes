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
        self.inv = dict()
        self.stk = dict()
        self.area = np.zeros((rows,cols))
        self.key_i = 1
        self.key_s = rows*cols+1

    def find_space(self,space):
        comparing = np.zeros(space)
        for i in range(self.rows-space[0]):
            for j in range(self.cols-space[1]):
                if False not in (self.area[i:i+space[0],j:j+space[1]] == comparing):
                    return [i,j]
        return [-1,-1]

    def add_object(self, obj):
        if obj.stackable:
            for i in self.stk.values():
                if i.base_id == obj.base_id:
                    if i.stack < i.max_stack:
                        i.stack += 1
                        break
            else:
                place = self.find_space(obj.space)
                if -1 in place:
                    print('No space in inventory')
                    return False
                else:
                    obj.pos_x = place[0]
                    obj.pos_x = place[1]
                    self.stk[self.key_s]=obj
                    self.area[place[0]:place[0]+obj.space[0],
                              place[1]:place[1]+obj.space[1]] = self.key_s
                    self.find_newks()
                    return True
        else:
            place = self.find_space(obj.space)
            if -1 in place:
                print('No space in inventory')
                return None
            else:
                obj.pos_x = place[0]
                obj.pos_x = place[1]
                self.inv[self.key_i]=obj
                self.area[place[0]:place[0]+obj.space[0],
                          place[1]:place[1]+obj.space[1]] = self.key_i
                self.find_newki()
                return True
                

                    
    def find_newks(self):
        pass
    def find_newki(self):
        pass
                    
                    
                        
                

class Object():
    """ Simple object"""

    def __init__(self, name, space, stackable, weight, base_id, max_stack, stack=1):
        self.name = name
        self.space = space
        self.stackable = stackable
        self.weight = weight
        self.stack = stack
        self.max_stack = max_stack
        self.base_id = base_id
        self.pos_x = 0
        self_pos_y = 0
            



