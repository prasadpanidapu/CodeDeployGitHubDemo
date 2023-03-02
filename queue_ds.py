# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:22:42 2023

@author: DELL
"""
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    q = Queue()
    print(q)
    q.enqueue("learning")
    q.enqueue("with")
    q.dequeue()
    q.enqueue("Linked")
    q.enqueue("In")
    q.dequeue()
    print(q)