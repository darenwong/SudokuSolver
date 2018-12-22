# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:58:49 2018

@author: Daren
"""
import numpy as np

# World hardest sudoku puzzle
board1 = np.array([[8, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 3, 6, 0, 0, 0, 0, 0],
                  [0, 7, 0, 0, 9, 0, 2, 0, 0],
                  [0, 5, 0, 0, 0, 7, 0, 0, 0],
                  [0, 0, 0, 0, 4, 5, 7, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 3, 0],
                  [0, 0, 1, 0, 0, 0, 0, 6, 8],
                  [0, 0, 8, 5, 0, 0, 0, 1, 0],
                  [0, 9, 0, 0, 0, 0, 4, 0, 0]])

board2 = np.array([[5, 1, 7, 6, 0, 0, 0, 3, 4],
                   [2, 8, 9, 0, 0, 4, 0, 0, 0],
                   [3, 4, 6, 2, 0, 5, 0, 9, 0],
                   [6, 0, 2, 0, 0, 0, 0, 1, 0],
                   [0, 3, 8, 0, 0, 6, 0, 4, 7],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 9, 0, 0, 0, 0, 0, 7, 8],
                   [7, 0, 3, 4, 0, 0, 5, 6, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]])

#Check if current board state is valid
def isValid(board):
    for i in board:
        for count in range(1,10):
            if list(i).count(count) > 1:
                return False
    for i in board.T:
        for count in range(1,10):
            if list(i).count(count) > 1:
                return False
    
    for x in range(3):
        for y in range(3):
            section = board[x*3:x*3+3, y*3:y*3+3]
            for count in range(1,10):
                if list(section.reshape(9)).count(count) > 1:
                    return False
    return True

#Find next empty grid cell to fill, returns -1,-1 if all are filled
def find_next_cell(board):
    for x in range(9):
        for y in range(9):
            if board[x,y] == 0:
                return x,y
    return -1,-1

#Solve the board recursively
def solver(board):
    global n
    n += 1
    
    x,y = find_next_cell(board)
    if x == -1:
        print('Number of iterations: ', n)
        print('Solved Board: ', board)
        return True
    
    for i in range(1,10):
        board[x,y] = i
        
        if isValid(board):
            solver(board) 
            if find_next_cell(board)[0] == -1:
                break
    else:
        board[x,y] = 0
        
    return board

#Set number of iterations to 0
n = 0  
solver(board2)             

# Results: Board1 requires 49559 iterations
#          Board2 requires 629 iterations
