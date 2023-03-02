# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:42:26 2023

@author: DELL
uses a priority queue containing f-value and (i, j) tuples along with
dictionaries for predessors and g-values 
"""

from helpers import read_maze, is_legal_pos, get_path, offsets
from priority_queue import Priority_Queue

def heuristic(a, b):
    """
    calculates the manhutten distance between two pairs of grid coordinates
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(maze, start, goal):
    pq = Priority_Queue()
    pq.put(start, 0)
    predessors = {start: None}
    g_values = {start: 0}
    
    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predessors, start, goal)
        for direction in offsets.keys():
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in g_values:
                new_cost = g_values[current_cell] + 1
                g_values[neighbor] = new_cost
                f_value = new_cost + heuristic(goal, neighbor)
                pq.put(neighbor, f_value)
                predessors[neighbor] = current_cell
    return None

if __name__ == "__main__":
    #test1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    print(result)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    #test2
    print("\n=========test2==========\n")
    maze = [[0, 0, "*", 0], [0, 0, 0, 0], [0, "*", 0, "*"], [0, 0, 0, 0]]
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    print(result)