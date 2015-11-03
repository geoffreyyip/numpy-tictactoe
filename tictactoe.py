################################################################################
# tictactoe.py - the first of many programs
# uses numpy arrays to represent an internal tictactoe board

# uses four global variables - board_arr, tutorial_arr, user_num, and comp_num

# Alright, time to test a partial commit

# This comment gets committed.

# This comment does not get committed.

import numpy as np
import random

initialize():
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