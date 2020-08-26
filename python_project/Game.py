# Main Python program:
# Note: Here we are assuming that you have already taken size of matrix and then values in matrix(0's & 1's only) from user.
#
# As a Developer write a program for matcing following constraints:
#
# You are given a two-dimensional array (matrix) of potentially unequal height and width
# containing only Os and 1s. Each 0 represents land, and each 1 represents part of a river.
# A river consists of any number of 1s that are either horizontally or vertically adjacent
# (but not diagonally adjacent). The number of adjacent 1s forming a river determine its
# size. Write a function that returns an array of the sizes of all rivers represented in the
# input matrix. Note that these sizes do not need to be in any particular order.
#
# Now from returned array of sizes You need to print "Guess the size of River" on each index, take input from user as guesses for each entry.
#
# If all entered sizes match then show You are the winner.
# If 60% of the inputs match with sizes in array of river sizes,show you got second position.
# else Show "Invest more money on Almonds, then come back".
#
# Now console should Ask if you wanted to play again:
# IF Yes : Redirect to the Matrix Input.
# Else : Exit
#
#
# Sample input:
# [1,0,0,1,0]
# (1,0,1,0,0)
# [0,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,1,0,
#
# Sizes of River = [1,2,2,2,5] note:  This should not be visible to the user , this a reference for accuracy of output.
#
#
# Sample output:
# Guess the size of River : input from user : note : This size should be compared with size present on specific or random index in river sizes array.
# Guess the size of River : input from user : 5
# you are the winner .
#

matrix = [
[1,0,0,1,0],
[1,0,1,0,0],
[0,0,1,0,1],
[1,0,1,0,1],
[1,0,1,1,0],
]

import numpy as np
from collections import deque
matrix = np.array([[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]])
ones_list = []
directions = [[1,0],[0,1],[-1,0],[0,-1]]
q = deque()
def game(input_mat):
    for i in range(0, len(input_mat)):
        for j in range(0, input_mat.shape[1]):
            if input_mat[i][j] == 1:
                input_mat[i][j] = 0
                q.append((i,j))
                riv_len = 0
                riv_len += 1
                while len(q) > 0:
                    qpop = q.pop()
                    trial_row = qpop[0]
                    trial_col = qpop[1]
                    for k in range(0, len(directions)):
                        trial_row1 = trial_row + directions[k][0]
                        trial_col1 = trial_col + directions[k][1]
                        if 0 <= trial_row1 < len(input_mat) and 0 <= trial_col1 < input_mat.shape[1]:
                            if input_mat[trial_row1][trial_col1] == 1:
                                input_mat[trial_row1][trial_col1] = 0
                                q.append((trial_row1, trial_col1))
                                riv_len += 1
                ones_list.append(riv_len)
                riv_len = 0
    ones_list.sort()
    return ones_list
def guess_size():
    guess_list = []
    for i in range(0, len(ones_list)):
        ask = input('Guess the size of River ' + str(i) + ':')
        guess_list.append(int(ask))
    correct_count = 0
    for j in range(0, len(guess_list)):
        if guess_list[j] in ones_list:
            correct_count += 1
    if correct_count < 0.6*len(ones_list):
        print("Invest more money on Almonds, then come back")
    elif 0.6*len(ones_list) <= correct_count < len(ones_list):
        print("you got second position")
    elif correct_count == len(ones_list):
        print("You are the winner")
ones_list = game(matrix)
guess_size()