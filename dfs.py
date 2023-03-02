# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:30:47 2023
DFS maze solver
@author: DELL

stack contains positions as (row, column) tuples. predessors are kept in dictionary
"""

from stack import Stack
from helpers import read_maze, is_legal_pos, get_path, offsets

def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predessors = {start: None}
    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predessors, start, goal)
        for direction in offsets.keys():
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0]+row_offset, current_cell[1]+col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predessors:
                stack.push(neighbor)
                predessors[neighbor] = current_cell
    return None

if __name__ == "__main__":
    #test1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    print(result)
    assert result == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    
    #test2
    