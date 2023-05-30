import random

# In a 9 by 9 empty sudoku board, row is marked from a to i, column is marked from 1 to 9. 
# Write a function in python to randomly select certain amount of cells from fat_list and also select the cells reflected by diagonal.
# Those cells will form a symmetric pattern. 
# Input: amount of cells to select between 1 to 16. Output: list of cells. 
# Expected output : ['a1', 'b2', 'c3', 'a4', 'b5', 'c6', 'a7', 'b8', 'c9', 'd1', 'e2', 'f3', 'd4', 'e5', 'f6', 'd7', 'e8', 'f9', 'g1', 'h2', 'i3', 'g4', 'h5', 'i6', 'g7', 'h8', 'i9']
fat_list = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']

import random

def generate_symmetric_pattern_diagonal(amount_to_select):
    fat_list = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']
                
    # Remove diagonal cells
    for i in range(9):
        cell = chr(ord('a') + i) + str(i + 1)
        fat_list.remove(cell)

    # Randomly select cells
    selected_cells = random.sample(fat_list, amount_to_select)

    # Get their diagonal reflections
    reflected_cells = [chr(ord('i') - (ord(cell[0]) - ord('a'))) + str(9 - int(cell[1]) + 1) for cell in selected_cells]

    return selected_cells + reflected_cells


def generate_symmetric_pattern_rotational(amount_to_select):
    fat_list = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']

    # Remove cells which are rotationally symmetrical to themselves
    rotationally_symmetric_cells = ['a1', 'a9', 'e5', 'i1', 'i9']
    for cell in rotationally_symmetric_cells:
        fat_list.remove(cell)

    # Randomly select cells
    selected_cells = random.sample(fat_list, amount_to_select)

    # Get their rotational reflections
    reflected_cells = [chr(ord('i') - (ord(cell[0]) - ord('a'))) + str(9 - int(cell[1]) + 1) for cell in selected_cells]

    return selected_cells + reflected_cells


def generate_symmetric_pattern_vertical(amount_to_select):
    fat_list = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']

    # Remove cells which are vertically symmetrical to themselves
    vertically_symmetric_cells = ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5', 'i5']
    for cell in vertically_symmetric_cells:
        fat_list.remove(cell)

    # Randomly select cells
    selected_cells = random.sample(fat_list, amount_to_select)

    # Get their vertical reflections
    reflected_cells = [cell[0] + str(10 - int(cell[1])) for cell in selected_cells]

    return selected_cells + reflected_cells


def generate_symmetric_pattern_horizontal(amount_to_select):
    fat_list = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9']

    # Remove cells which are horizontally symmetrical to themselves
    horizontally_symmetric_cells = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9']
    for cell in horizontally_symmetric_cells:
        fat_list.remove(cell)

    # Randomly select cells
    selected_cells = random.sample(fat_list, amount_to_select)

    # Get their horizontal reflections
    reflected_cells = [chr(ord('i') - (ord(cell[0]) - ord('a'))) + cell[1] for cell in selected_cells]

    return selected_cells + reflected_cells


# Conclude the above functions into one
def generate_symmetric_pattern_random(amount_to_select):
    dice = random.randint(0, 3)
    if dice == 0:
        return generate_symmetric_pattern_diagonal(amount_to_select)
    elif dice == 1:
        return generate_symmetric_pattern_vertical(amount_to_select)
    elif dice == 2:
        return generate_symmetric_pattern_horizontal(amount_to_select)
    elif dice == 3:
        return generate_symmetric_pattern_rotational(amount_to_select)