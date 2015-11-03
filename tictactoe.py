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
    
    
def return_open_slots():
# Checks for open slots using Boolean arrays.
# Important when checking for winner (if draw) and checking if user's input...
# ...is valid
    open_slots = []

    bool_arr = (board_arr == 3)
    flat_bool_arr = bool_arr.flatten()
    
    # is spot taken by 3's? If so, then spot is open.
    # appends (i + 1) because inputs are indexed to 1
    for i in range(0, len(flat_bool_arr)):
        if flat_bool_arr == True:
            open_slots.append(i + 1)
            
    return open_slots


def terminate(last_played_num):
# if last played number is user's number, declares user to be winner
# if last played number is comp's number, declares comp to be winner
# if return_open_slots() came up blank, declares draw
    if last_played_num == user_num:
        print("You win!")
    elif last_played_num == comp_num:
        print("You lost!")
    elif last_played_num == "Draw!":
        print("Draw!")
        
    input("Play again? \nPress Enter to play again.")
    initialize()
        
def check_for_winner(last_played_num):
# Scans rows, columns, and diagonals for last-played number
# Ex. if 1 was the last number played, this function would scan for 1's
# Declares draw is open_slots is blank
# Else proceeds to next turn
    
    if return_open_slots == []:
    # Checks if no open slots
        terminate("Draw!")
        
    for i in range(0, 3):
    # Checks rows and columns for match
        rows_win = (board_arr[i, :] == last_played_num).all()
        cols_win = (board_arr[:, i] == last_played_num).all()
        
        if rows_win or cols_win:
            termiante(last_played_num)
            
    diag1_win = (np.diag(board_arr) == last_played_num).all()
    diag2_win = (np.diag(np.fliplr(board_arr)) == last_played_num).all()
    
    if diag1_win or diag2_win:
    # Checks both diagonals for match
        terminate(last_played_num)
            
    next_turn(last_played_num)
    
    
def next_turn(last_played_num):
    if last_played_num == user_num:
        comp_turn()
    elif last_played_num == comp_num:
        user_turn()


def place_letter(current_num, current_input):
# Takes comp_num and comp_choice (or user_num and user_choice)...
# ...and inputs that into the global board_arr
# Current_input is either randomly chosen by computer or input by user
# Current_num is either user_num or comp_num
    index = np.where(tutorial_arr == current_input)
    board_arr[index] = current_num

    
# TODO: LIST OPEN SLOTS ON ASCII BOARD
def user_turn():
    display_board()
    
    user_input = input("Pick an open slot: ")
    user_input = int(user_input)
    
    if user_input in return_open_slots():
        place_letter(user_num, user_input)
    else:
        print("That's not a open slots.")
        user_turn()
        
    check_for_winner(user_num)
    

def comp_turn()
# Randomly chooses from open_slots to place its letter    
    open_slots = return_open_slots()
    comp_choice = random.choice(open_slots)
    place_letter(comp_num, comp_input)
    check_for_winner(comp_num)
    