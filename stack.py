# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:23:32 2023

@author: DELL
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not len(self.items)
    
    def push(self, item):
        self.items.append(item)
        #return self.items
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)