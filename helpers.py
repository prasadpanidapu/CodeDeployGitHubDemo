# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:57:06 2023

@author: DELL
"""

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
    }

def read_maze(file_name):
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_col_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_col_top_row:
                    print("maze is not rectangular")
                    raise SystemExit
            return maze
    except IOError:
        print("there is a problem with file you have selcted")
        raise SystemExit

def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"

def get_path(predessors, start, goal):
    current_pos = goal
    path = []
    while current_pos != start:
        path.append(current_pos)
        current_pos = predessors[current_pos]
    path.append(start)
    path.reverse()
    return path