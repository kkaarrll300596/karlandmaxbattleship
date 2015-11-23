# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:24:37 2015

@author: Maxime
"""
#%%
class batteship:
    def __init__(self):
        pass


class navire:
    def __init__(self, longeur):
        pass


class grid:
    def __init__(self, m=10, n=10):
        assert m > 0 and n > 0
        self.n = n
        self.m = m
        self.setValues(0 for _ in range(m*n))
    
    def setValues(self, iterable):
        data = list(iterable)
        if len(data) != self.m*self.n:
            raise ValueError()
        self.data = data
        return self
    
    def __getitem__(self, index):
        i, j = index
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            raise IndexError()
        return self.data[i*self.n + j]
    
    def __setitem__(self, index, x):
        i, j = index
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            raise IndexError()
        self.data[i*self.n + j] = x
        
        
class iafaible(player):
    import random as r
    #while True:
        #shoot((r.randint(0, self.m), r.randint(0, self.n)))
    pass


class iaforte(player):
    import random as r
    while True:
        target = (r.randint(0, self.m), r.randint(0, self.n)) 
        result = shoot(target)
        if result == 1:
            shoot(around(target))
        else: pass
    
    
def around(position):
    i, j = position
    return [grid[i-1, j-1], grid[i-1, j+1], grid[i+1, j-1], grid[i+1, j+1]
    
                
        
        
A = grid(10,10)
around(1,2)

#%%

#%%
def around(position):
    i, j = position
    return [grid[i-1, j-1], grid[i-1, j+1], grid[i+1, j-1], grid[i+1, j+1]
    
#%%

