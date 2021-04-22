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
        self.on_tranf = None

    def find_space_old(self, space): #O(N**2 * M**2)
        """ Find the location of a free space in the inventory""" 
        comparing = np.zeros(space)
        for i in range(self.rows-space[0]+1):
            for j in range(self.cols-space[1]+1):
                if False not in (self.area[i:i+space[0],j:j+space[1]] == comparing):
                    return [i,j]
        return [-1,-1]

    def find_space(self, space): #O(N**2 * M)
        """ Find the location of a free space in the inventory"""
        comparing = np.zeros(space)
        for i in range(self.rows-space[0]+1):
            for j in range(self.cols-space[1]+1):
                if False not in (self.area[i,j:j+space[1]] == comparing[0,:]):
                    if False not in (self.area[i:i+space[0],j:j+space[1]] == comparing):
                        return [i,j]
        return [-1,-1]

    def add_object(self, objc):
        """ Add a new object in the inventory"""
        obj = objc.copy()
        if obj.stackable:
            for i in self.stk.values():
                if i.base_id == obj.base_id:
                    if i.stack < i.max_stack:
                        if obj.stack + i.stack <i.max_stack:
                            print(obj.stack + i.stack)
                            i.stack += obj.stack
                            break
                        else:
                            obj.stack -= (i.max_stack - i.stack)
                            i.stack = i.max_stack
                            
            else:
                place = self.find_space(obj.space)
                if -1 in place:
                    print('No space in inventory')
                    return False
                else:
                    obj.pos_x = place[0]
                    obj.pos_y = place[1]
                    self.stk[self.key_s]=obj
                    self.area[place[0]:place[0]+obj.space[0],
                              place[1]:place[1]+obj.space[1]] = self.key_s
                    self.find_newks()
                    return True
        else:
            place = self.find_space(obj.space)
            if -1 in place:
                print('No space in inventory')
                return False
            else:
                obj = obj.copy()
                obj.pos_x = place[0]
                obj.pos_y = place[1]
                self.inv[self.key_i]=obj
                self.area[place[0]:place[0]+obj.space[0],
                          place[1]:place[1]+obj.space[1]] = self.key_i
                self.find_newki()
                return True
                

                    
    def find_newks(self):
        """ Find new key to stackable itens"""
        for i in range(self.key_s+1,2*self.rows*self.cols+1):
            if i not in self.stk.keys():
                self.key_s = i
                break
        else:
            for i in range(self.rows*self.cols+1,self.key_s):
                self.key_s = i
                break
            else:
                print("Something wrong is not right in da key_s allocation")
                
    def find_newki(self):
        """ Find new key to inventory itens"""
        for i in range(self.key_i+1,self.rows*self.cols+1):
            if i not in self.inv.keys():
                self.key_i = i
                break
        else:
            for i in range(1,self.key_i):
                if i not in self.inv.keys():
                    self.key_i = i
                    break
            else:
                print("Something wrong is not right in da key_s allocation")
                
    def remove_item(self, place, qtt=1):
        """ Remove a iten from the inventory"""
        key = self.area[place[0], place[1]]
        print(key)
        if key == 0:
            return False
        elif key < self.rows*self.cols+1:
            self.relase_space(self.inv[key])
            pivot = self.inv[key].copy()
            del(self.inv[key])
            return pivot
        else:
            print(self.stk[key].stack)
            if self.stk[key].stack-qtt <= 0:
                self.relase_space(self.stk[key])
                pivot = self.stk[key].copy()
                del(self.stk[key])
                return pivot
            else:
                print('foi')
                self.stk[key].stack -= qtt
                pivot = self.stk[key].copy()
                pivot.stack = qtt
                return pivot

    def relase_space(self, obj):
        """ Clear inv space"""
        print(obj.pos_x)
        self.area[obj.pos_x:obj.pos_x+obj.space[0],
                  obj.pos_y:obj.pos_y+obj.space[1]] = 0

##    def rc_mouse(self,place):
##        
##        if self.on_tranf == None:
##            self.on_tranf = self.remove_item(place)
##        else:
##            if self.on_tranf.stackable:
##                if self
                    
                    
                        
                

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
        self.pos_y = 0

    def copy(self):
        return Object(self.name, (self.space[0],self.space[1]), self.stackable, self.weight,
                      self.base_id, self.max_stack, self.stack)
            



