# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:16:47 2023

@author: DELL
"""

import heapq

class Priority_Queue:
    
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return not self.elements
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)
    
if __name__ == "__main__":
    q = Priority_Queue()
    print(q)
    q.put([0,0], 5)
    q.put("b", 6)
    print(q)
    q.get()
    print(q)
    print(q.is_empty())
    q.get()
    print(q.is_empty())