
import random
from constraint import ExactSumConstraint, MinConflictsSolver, Problem, AllDifferentConstraint

def more_than(a, b):
    return a > b

def is_odd(a):
    return a % 2 == 1

def is_even(a):
    return a % 2 == 0

# Skyscraper logic
def skyscraper_x(y):
    x = 0  
    max_seen = 0  
    for i in y:  
        if i > max_seen:  
            x += 1  
            max_seen = i  
    return x  # visibility count

# print(skyscraper_x([1, 3, 2, 4, 5, 9, 7, 6, 8]))  # Expected output: 5
# print(skyscraper_x([9, 8, 7, 6, 5, 4, 3, 2, 1]))  # Expected output: 1
# print(skyscraper_x([5, 2, 1, 6, 3, 9, 4, 7, 8]))  # Expected output: 3

def skyscraper_1(*args):
    return skyscraper_x(list(args)) == 1

def skyscraper_2(*args):
    return skyscraper_x(list(args)) == 2

def skyscraper_3(*args):
    return skyscraper_x(list(args)) == 3

def skyscraper_less_than_3(*args):
    return skyscraper_x(list(args)) < 3

def skyscraper_more_than_3(*args):
    return skyscraper_x(list(args)) > 3

def skyscraper_4(*args):
    return skyscraper_x(list(args)) == 4

def skyscraper_less_than_4(*args):
    return skyscraper_x(list(args)) < 4

def skyscraper_more_than_4(*args):
    return skyscraper_x(list(args)) > 4

def skyscraper_5(*args):
    return skyscraper_x(list(args)) == 5

def skyscraper_less_than_5(*args):
    return skyscraper_x(list(args)) < 5

def skyscraper_more_than_5(*args):
    return skyscraper_x(list(args)) > 5

def skyscraper_6(*args):
    return skyscraper_x(list(args)) == 6

def skyscraper_less_than_6(*args):
    return skyscraper_x(list(args)) < 6

def skyscraper_more_than_6(*args):
    return skyscraper_x(list(args)) > 6

def skyscraper_7(*args):
    return skyscraper_x(list(args)) == 7

def skyscraper_8(*args):
    return skyscraper_x(list(args)) == 8

def skyscraper_9(*args):
    return skyscraper_x(list(args)) == 9

# =================================================================================================
# Initialize

problem = Problem()

def initialize_problem(problem):

    problem.reset()
    problem.addVariables(["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"], range(1, 10))
    problem.addVariables(["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"], range(1, 10))
    problem.addVariables(["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"], range(1, 10))

    problem.addVariables(["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9"], range(1, 10))
    problem.addVariables(["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9"], range(1, 10))
    problem.addVariables(["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"], range(1, 10))

    problem.addVariables(["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"], range(1, 10))
    problem.addVariables(["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9"], range(1, 10))
    problem.addVariables(["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9"], range(1, 10))

    # Each row has different values
    problem.addConstraint(AllDifferentConstraint(), ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"])
    problem.addConstraint(AllDifferentConstraint(), ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9"])
    problem.addConstraint(AllDifferentConstraint(), ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"])

    problem.addConstraint(AllDifferentConstraint(), ["d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9"])
    problem.addConstraint(AllDifferentConstraint(), ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9"])
    problem.addConstraint(AllDifferentConstraint(), ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"])

    problem.addConstraint(AllDifferentConstraint(), ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"])
    problem.addConstraint(AllDifferentConstraint(), ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9"])
    problem.addConstraint(AllDifferentConstraint(), ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9"])

    # Each colum has different values
    problem.addConstraint(AllDifferentConstraint(), ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1"])
    problem.addConstraint(AllDifferentConstraint(), ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2"])
    problem.addConstraint(AllDifferentConstraint(), ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3"])

    problem.addConstraint(AllDifferentConstraint(), ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4"])
    problem.addConstraint(AllDifferentConstraint(), ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "i5"])
    problem.addConstraint(AllDifferentConstraint(), ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "i6"])

    problem.addConstraint(AllDifferentConstraint(), ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "i7"])
    problem.addConstraint(AllDifferentConstraint(), ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "i8"])
    problem.addConstraint(AllDifferentConstraint(), ["a9", "b9", "c9", "d9", "e9", "f9", "g9", "h9", "i9"])

    # Each 3x3 box has different values
    problem.addConstraint(AllDifferentConstraint(), ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"])
    problem.addConstraint(AllDifferentConstraint(), ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"])
    problem.addConstraint(AllDifferentConstraint(), ["g1", "g2", "g3", "h1", "h2", "h3", "i1", "i2", "i3"])

    problem.addConstraint(AllDifferentConstraint(), ["a4", "a5", "a6", "b4", "b5", "b6", "c4", "c5", "c6"])
    problem.addConstraint(AllDifferentConstraint(), ["d4", "d5", "d6", "e4", "e5", "e6", "f4", "f5", "f6"])
    problem.addConstraint(AllDifferentConstraint(), ["g4", "g5", "g6", "h4", "h5", "h6", "i4", "i5", "i6"])

    problem.addConstraint(AllDifferentConstraint(), ["a7", "a8", "a9", "b7", "b8", "b9", "c7", "c8", "c9"])
    problem.addConstraint(AllDifferentConstraint(), ["d7", "d8", "d9", "e7", "e8", "e9", "f7", "f8", "f9"])
    problem.addConstraint(AllDifferentConstraint(), ["g7", "g8", "g9", "h7", "h8", "h9", "i7", "i8", "i9"])

    # Each diagonal has different values
    # problem.addConstraint(AllDifferentConstraint(), ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8", "i9"])
    # problem.addConstraint(AllDifferentConstraint(), ["a9", "b8", "c7", "d6", "e5", "f4", "g3", "h2", "i1"])
    # problem.addConstraint(AllDifferentConstraint(), ["a3", "b4", "c5", "d6", "e7", "f8", "g9"])
    # problem.addConstraint(AllDifferentConstraint(), ["a7", "b6", "c5", "d4", "e3", "f2", "g1"])
    # problem.addConstraint(AllDifferentConstraint(), ["c1", "d2", "e3", "f4", "g5", "h6", "i7"])
    # problem.addConstraint(AllDifferentConstraint(), ["c9", "d8", "e7", "f6", "g5", "h4", "i3"])

    # Some example constraints

    # Constraint: cells that has given values
    # problem.addConstraint(
    #     lambda val : val == 4, ["a1"] 
    # )

    # Constraint: more than/less than
    # problem.addConstraint(
    #     lambda val1, val2 : val1 > val2, ["a1", "a2"]
    # )

    # Constraint: consecutive cells
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["b2", "c2"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["b3", "c3"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["b4", "c4"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["g6", "h6"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["g7", "h7"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["g8", "h8"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["b7", "b8"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["c7", "c8"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["d7", "d8"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["h2", "h3"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["g2", "g3"]
    # )
    # problem.addConstraint(
    #     lambda val1, val2 : abs(val1 - val2) == 1, ["f2", "f3"]
    # )
    # Constraint: sum exactly to certain value, killer sudoku
    # problem.addConstraint(ExactSumConstraint(24), ["c1", "c2", "d1", "d2"])

    # Constraint: only even value in cell
    # problem.addConstraint(is_even, ["i9"])

    # Constraint: skyscraper row/column/diagonal, skyscraper sudoku
    # working correctly, extremely slow, may takes years or decades to run.
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "i3"]
    # )
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "i4"]
    # )
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["c9", "c8", "c7", "c6", "c5", "c4", "c3", "c2", "c1"]
    # )
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["d9", "d8", "d7", "d6", "d5", "d4", "d3", "d2", "d1"]
    # )
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["i7", "h7", "g7", "f7", "e7", "d7", "c7", "b7", "a7"]
    # )
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["i6", "h6", "g6", "f6", "e6", "d6", "c6", "b6", "a6"]
    # )
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9"]
    # )
    # problem.addConstraint(
    #     skyscraper_less_than_4, ["g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9"]
    # )
# ==============================================================================
# Solver

def solve_sudoku(get_one_solution=True):
    if get_one_solution: # If we only want one solution
        one_solution = problem.getSolution() # <class 'dict'>
        if one_solution is None:
            print("No solution found")
        return one_solution

    else: # If we want all solutions
        all_solutions = problem.getSolutions() # <class 'list'> of <class 'dict'>
        if len(all_solutions) == 0:
            print("No solutions found")
        else:
            print("Number of solutions found: ", len(all_solutions))
        return all_solutions

# Find all solutions and number of solutions and write to a log file
def find_all_solutions_and_add_to_log_file(file_name="solutions.txt"):
    all_solutions = solve_sudoku(get_one_solution=False)
    if all_solutions is not None:
        with open(file_name, "a") as f:
            # f.write("Number of solutions found: " + str(len(all_solutions)) + "\n")
            for solution in all_solutions:
                f.write(str(solution) + "\n")
                # f.write("-"*20 + "\n")
    # else:
    #     with open("log.txt", "a") as f:
    #         f.write("No solutions found\n")

# Find 1 solution and write to a log file
def find_one_solution_and_add_to_log_file(file_name="solutions.txt"):
    one_solution = solve_sudoku(get_one_solution=True)
    if one_solution is not None:
        with open(file_name, "a") as f:
            f.write(str(one_solution) + "\n")
            # f.write("-"*20 + "\n")
    # else:
    #     with open("log.txt", "a") as f:
    #         f.write("No solution found\n")

#===============================================================================
# Print
# print_solution(solve_sudoku())

def print_solution(solution_dict):
    if solution_dict is None:
        print("No solution found")
    else:
        for row in 'abcdefghi':
            for col in '123456789':
                key = row+col
                if key in solution_dict:
                    print(solution_dict[key], end=' ')
                else:
                    print('_', end=' ')  # print underscore for missing values
                if col == '3' or col == '6':
                    print('| ', end='')
            print()
            if row == 'c' or row == 'f':
                print("-"*21)

def print_puzzle(puzzle_list):
    # Initialize empty board
    puzzle_dict = {chr(i + 97) + str(j + 1): " " for i in range(9) for j in range(9)}

    # Populate board
    for cell, value in puzzle_list:
        puzzle_dict[cell] = value

    # Print board
    for row in 'abcdefghi':
        for col in '123456789':
            print(puzzle_dict[row+col], end=' ')
            if col == '3' or col == '6':
                print('| ', end='')
        print()
        if row == 'c' or row == 'f':
            print("-"*21)


# ==============================================================================
# We do not care about whether the sudoku has solution or not in the following two functions
def populate_sudoku(amount):
    board = [[0 for _ in range(9)] for _ in range(9)]
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    
    def is_valid(board, row, col, num):
        # check the row
        for x in range(9):
            if board[row][x] == num:
                return False

        # check the column
        for x in range(9):
            if board[x][col] == num:
                return False

        # check the box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True
    
    for _ in range(amount):
        while positions:
            row, col = positions.pop()
            num = random.randint(1, 9)
            if is_valid(board, row, col, num):
                board[row][col] = num
                break

    output = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                output.append((chr(i + 97) + str(j + 1), board[i][j]))
                
    return output

# cell_list_example = ["a1", "b5", "c9", "d4", "e2", "f7", "g6", "h3", "i8"]
def populate_sudoku_with_cells(cell_list):
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    def is_valid(board, row, col, num):
        # check the row
        for x in range(9):
            if board[row][x] == num:
                return False

        # check the column
        for x in range(9):
            if board[x][col] == num:
                return False

        # check the box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True


    for cell in cell_list:
        row = ord(cell[0]) - 97
        col = int(cell[1:]) - 1
        num = random.randint(1, 9)
        while not is_valid(board, row, col, num):
            num = random.randint(1, 9)
        board[row][col] = num
    
    output = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                output.append((chr(i + 97) + str(j + 1), board[i][j]))

    return output


# ==============================================================================
# Generator

# generate_puzzle_from_solution_data(24, get_log_file_line(1))
def generate_puzzle_from_solution_data(amount, solution_data):
    cell_values = list(solution_data.items())
    random.shuffle(cell_values)
    cell_values = cell_values[:amount]
    return cell_values

# cell_list_example = ["a1", "b5", "c9", "d4", "e2", "f7", "g6", "h3", "i8"]
# solution_data_example = {'a5': 8, 'a9': 2, 'b1': 2, 'b2': 3, 'b6': 9, 'b7': 8, 'c1': 8, 'c5': 1, 'c9': 6, 'd1': 9, 'd7': 6, 'd8': 4, 'e1': 1, 'e2': 5, 'f4': 4, 'f6': 8, 'g7': 9, 'g9': 1, 'h5': 4, 'h7': 7, 'h8': 6, 'i3': 7, 'i6': 6, 'i9': 5, 'b9': 4, 'c7': 5, 'a7': 3, 'e7': 2, 'f7': 1, 'i7': 4, 'i1': 3, 'h1': 5, 'b8': 1, 'a8': 9, 'c8': 7, 'b3': 6, 'a1': 7, 'f1': 6, 'g1': 4, 'a2': 1, 'a3': 5, 'a4': 6, 'a6': 4, 'b4': 5, 'b5': 7, 'c2': 4, 'c3': 9, 'c4': 2, 'c6': 3, 'e6': 7, 'd4': 3, 'e4': 9, 'e5': 6, 'd3': 2, 'd5': 5, 'd6': 1, 'f2': 7, 'd2': 8, 'd9': 7, 'f3': 3, 'e3': 4, 'f5': 2, 'f8': 5, 'f9': 9, 'g3': 8, 'g4': 7, 'g5': 3, 'g8': 2, 'g2': 6, 'g6': 5, 'h3': 1, 'h4': 8, 'h6': 2, 'h2': 9, 'h9': 3, 'e9': 8, 'e8': 3, 'i2': 2, 'i4': 1, 'i5': 9, 'i8': 8}
# return : [('a1', 7), ... ]
def generate_puzzle_from_solution_data_cells(cell_list, solution_data):
    # Initialize an empty list to store the puzzle data
    cell_values = []

    # Iterate over the cell_list
    for cell in cell_list:
        # Get the value of the current cell from the solution_data
        value = solution_data.get(cell)

        # Add the current cell and its value as a tuple to the puzzle list
        cell_values.append((cell, value))
        
    # Return the puzzle list
    return cell_values


def find_puzzle_with_generate_puzzle_from_solution_data_cells(cell_list, loop=1, unique_solution=False):
    solution_data = get_log_file_line(random.randint(1, 13685))
    attempts = 0
    solution_data_switch = 0
    puzzle = generate_puzzle_from_solution_data_cells(cell_list, solution_data)
    assign_values(puzzle)
    
    if unique_solution:
        solutions = solve_sudoku(get_one_solution=False)
        while len(solutions) != 1:
            attempts += 1
            solution_data_switch += 1
            if solution_data_switch >= loop:
                solution_data_switch = 0
                solution_data = get_log_file_line(random.randint(1, 13685))
                print("Switched solution data")
            puzzle = generate_puzzle_from_solution_data_cells(cell_list, solution_data)
            assign_values(puzzle)
            solutions = solve_sudoku(get_one_solution=False)
        return solutions[0], puzzle, attempts
    else:
        solution = solve_sudoku()
        while solution is None:
            attempts += 1
            solution_data_switch += 1
            if solution_data_switch >= loop:
                solution_data_switch = 0
                solution_data = get_log_file_line(random.randint(1, 13685))
                print("Switched solution data")
            puzzle = generate_puzzle_from_solution_data_cells(cell_list, solution_data)
            assign_values(puzzle)
            solution = solve_sudoku()
        
        return solution, puzzle, attempts


def find_puzzle_with_generate_puzzle_from_solution_data(amount, loop=100):
    solution_data = get_log_file_line(random.randint(1, 13685))
    attempts = 0
    solution_data_switch = 0
    puzzle = generate_puzzle_from_solution_data(amount, solution_data)
    assign_values(puzzle)
    solution = solve_sudoku()
    while solution is None:
        attempts += 1
        solution_data_switch += 1
        puzzle = generate_puzzle_from_solution_data(amount, solution_data)
        assign_values(puzzle)
        solution = solve_sudoku()
        if solution_data_switch > loop:
            solution_data_switch = 0
            solution_data = get_log_file_line(random.randint(1, 13685))
            print("Switched solution data")
    # print("Solution: ")
    # print_solution(solution)
    # print("\nPuzzle: ")
    # print_puzzle(puzzle) 
    # print("\nAttempts: ")
    # print(attempts)
    return solution, puzzle, attempts

def find_puzzle_with_generate_puzzle_from_solution_data_with_unique_solution(amount, loop=100):
    solution_data = get_log_file_line(random.randint(1, 13685))
    attempts = 0
    solution_data_switch = 0
    puzzle = generate_puzzle_from_solution_data(amount, solution_data)
    assign_values(puzzle)
    solutions = solve_sudoku(get_one_solution=False)
    while len(solutions) != 1:
        attempts += 1
        solution_data_switch += 1
        puzzle = generate_puzzle_from_solution_data(amount, solution_data)
        assign_values(puzzle)
        solutions = solve_sudoku(get_one_solution=False)
        if solution_data_switch > loop:
            solution_data_switch = 0
            solution_data = get_log_file_line(random.randint(1, 13685))
            print("Switched solution data")
    # print("Solution: ")
    # print_solution(solutions[0])
    # print("\nPuzzle: ")
    # print_puzzle(puzzle) 
    # print("\nAttempts: ")
    # print(attempts)
    return solutions[0], puzzle, attempts

def assign_value(cell, value):
    problem.addConstraint(
        lambda val : val == value, [cell] 
    )

def assign_values(cell_values):
    problem.reset()
    initialize_problem(problem)
    for cell, value in cell_values:
        assign_value(cell, value)

def find_puzzle_with_given_cells_with_at_least_one_solution(cell_list):
    attempts = 0
    puzzle = populate_sudoku_with_cells(cell_list)
    assign_values(puzzle)
    solution = solve_sudoku()
    while solution is None:
        attempts += 1
        puzzle = populate_sudoku_with_cells(cell_list)
        assign_values(puzzle)
        solution = solve_sudoku()
    return solution, puzzle, attempts

def find_puzzle_with_given_cells_with_unique_solution(cell_list):
    attempts = 0
    puzzle = populate_sudoku_with_cells(cell_list)
    assign_values(puzzle)
    solutions = solve_sudoku(get_one_solution=False)
    while len(solutions) != 1:
        attempts += 1
        puzzle = populate_sudoku_with_cells(cell_list)
        assign_values(puzzle)
        solutions = solve_sudoku(get_one_solution=False)
    return solutions[0], puzzle, attempts

def find_puzzle_with_given_cells_with_at_least_one_solution_and_print(cell_list):
    x, y, z = find_puzzle_with_given_cells_with_at_least_one_solution(cell_list)
    print("Solution: ")
    print_solution(x)
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)

def find_puzzle_with_given_cells_with_unique_solution_and_print(cell_list):
    x, y, z = find_puzzle_with_given_cells_with_unique_solution(cell_list)
    print("Solution: ")
    print_solution(x)
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)

def find_puzzle_with_at_least_one_solution(amount=24):
    attempts = 0
    puzzle = populate_sudoku(amount)
    assign_values(puzzle)
    solution = solve_sudoku()
    while solution is None:
        attempts += 1
        puzzle = populate_sudoku(amount)
        assign_values(puzzle)
        solution = solve_sudoku()
    return solution, puzzle, attempts

def find_puzzle_with_unique_solution(amount=24):
    attempts = 0
    puzzle = populate_sudoku(amount)
    assign_values(puzzle)
    solutions = solve_sudoku(get_one_solution=False)
    while len(solutions) != 1:
        attempts += 1
        puzzle = populate_sudoku(amount)
        assign_values(puzzle)
        solutions = solve_sudoku(get_one_solution=False)
    return solutions[0], puzzle, attempts

def find_puzzle_with_at_least_one_solution_and_print(amount=24):
    x, y, z = find_puzzle_with_at_least_one_solution(amount)
    print("Solution: ")
    print_solution(x)
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)

def find_puzzle_with_unique_solution_and_print(amount=24):
    x, y, z = find_puzzle_with_unique_solution(amount)
    print("Solution: ")
    print_solution(x)
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)

# return certain line of the log file, should be a dict
def get_log_file_line(line_number, file_name="solutions.txt"):
    with open(file_name, "r") as f:
        lines = f.readlines()
        return eval(lines[line_number - 1])

def create_sudoku_database(loop, file_name, add_all_solutions=False):
    for i in range(0, loop):
        puzzle = populate_sudoku(random.randint(18, 30))
        assign_values(puzzle)
        if not add_all_solutions:
            find_one_solution_and_add_to_log_file(file_name)
        else:
            find_all_solutions_and_add_to_log_file(file_name)

def main():
    find_puzzle_with_given_cells_with_at_least_one_solution_and_print(["a1", "a2", "d7"])
    # find_puzzle_with_unique_solution_and_print(18)
    # find_puzzle_with_at_least_one_solution_and_print(0)
    # find_puzzle_with_generate_puzzle_from_solution_data(32)
    
if __name__ == "__main__":
    main()



