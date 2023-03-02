# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:52:49 2023

@author: DELL
queue contains positions as (row, column) tuples. predessors are kept in dictionary
"""

from helpers import read_maze, is_legal_pos, get_path, offsets
from queue_ds import Queue

def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predessors = {start: None}
    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return get_path(predessors, start, goal)
        for direction in offsets.keys():
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0]+row_offset, current_cell[1]+col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predessors:
                queue.enqueue(neighbor)
                predessors[neighbor] = current_cell
    return None

if __name__ == "__main__":
    #test1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    print(result)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    #test2
    print("\n=========test2==========\n")
    maze = [[0, 0, "*", 0], [0, 0, 0, 0], [0, "*", 0, "*"], [0, 0, 0, 0]]
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    print(result)