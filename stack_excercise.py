# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:38:19 2023

@author: DELL
"""

import stack

string = 'Naga Vara Prasad'
rev_string = ''
s = stack.Stack()
for char in string:
    s.push(char)
while not s.is_empty():
    rev_string += s.pop()
print(rev_string)