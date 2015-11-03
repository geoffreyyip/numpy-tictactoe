################################################################################
# tictactoe.py - the first of many programs
# uses numpy arrays to represent an internal tictactoe board

# uses four global variables - board_arr, tutorial_arr, user_num, and comp_num

# Alright, time to test a partial commit

# This comment gets committed.

# This comment does not get committed.

import numpy as np
import random

# Creates blank 3x3 array. Randomizes who goes first.
# TODO: ADD A TUTORIAL PROGRAM
def initialize():
    global board_arr
    global tutorial_arr
    
    # 0's act as O's
    # 1's act as X's
    # 3's act as placeholders for blank spots
    board_arr = np.array([[3, 3, 3],
                          [3, 3, 3],
                          [3, 3, 3]])
    tutorial_arr = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])
    
    global user_num
    global comp_num
    
    # Flip a coin to see who goes first with X's
    if np.random.randint(0, 2) == 0:
        user_num = 0
        comp_num = 1
        print("Computer goes first.")
        comp_turn()
        
    elif np.random.randint(0, 2) == 1:
        user_num = 1
        comp_num = 0
        print("You go first.")
        user_turn()

        
# Converts internal numpy array into a visual ASCII board.       
def display_board():
    board_list = []
    
    # loops through flattened board array to scan for 0's, 1's and 3's
    # converts them into O's, X's, and blank spots
    internal_arr = board_arr.flatten()
    for i in range(0, 9)
       if internal_arr[i] == 0:
           board_list.append('O')
       elif internal_arr[i] == 1:
           board_list.append('X')
       elif internal_arr[i] == 3:
           board_list.append(' ')
       else:
           raise Exception("display_board Error")
    
    # inputs O's, X's, and blank spots into an ASCII tictactoe board
    print("""
 {} | {} | {}
---+---+---
 {} | {} | {}
---+---+---
 {} | {} | {}

""".format(*board_list))
    