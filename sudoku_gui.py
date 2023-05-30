import pygame
import pygame_gui
import ctypes
from sudoku_designer import *
from pattern_generator import *

# Disable windows app scaling 
ctypes.windll.user32.SetProcessDPIAware()

pygame.init()

pygame.display.set_caption('Sudoku')
window_surface = pygame.display.set_mode((1200, 900))
ui_manager = pygame_gui.UIManager((1200, 900), "theme_light_green.json")

background = pygame.Surface((1200, 900))
background.fill(ui_manager.ui_theme.get_colour('dark_bg'))

# Sudoku grid size
grid_size = 9
cell_size = 60 # size of each sudoku cell
start_x = 100 # starting x-coordinate of sudoku board
start_y = 100 # starting y-coordinate of sudoku board

# Draw Sudoku grid
for i in range(grid_size+1):
    # Horizontal lines
    pygame.draw.line(background, (0, 0, 0), (start_x, start_y + i * cell_size), 
                        (start_x + grid_size * cell_size, start_y + i * cell_size), 2 if i % 3 else 6)
    # Vertical lines
    pygame.draw.line(background, (0, 0, 0), (start_x + i * cell_size, start_y), 
                        (start_x + i * cell_size, start_y + grid_size * cell_size), 2 if i % 3 else 6)

# Draw input area
# Initialize cell dictionary to keep track of all cells
cells = {}
solution = {}
# Loop through all grid rows and columns
for i in range(grid_size):
    for j in range(grid_size):
        # Compute cell position and size
        pos = (start_x + j * cell_size + 13, start_y + i * cell_size + 4)
        size = (46, 54)

        # Generate cell id (a1, a2, ..., i9)
        cell_id = chr(ord('a') + i) + str(j+1)

        # Create UITextEntryLine for this cell
        cells[cell_id] = pygame_gui.elements.UITextEntryLine(pygame.Rect(pos, size), ui_manager)
        cells[cell_id].allowed_characters = "123456789"
        cells[cell_id].set_text_length_limit(1)

def set_input_value(cell_id, value):
    cells[cell_id].set_text(value)

def reset_board():
    for cell_id in cells:
        cells[cell_id].set_text("")

# Solution: 
# {'e5': 9, 'a1': 4, 'a9': 8, 'i1': 7, 'i9': 6, 'b2': 8, 'c3': 7, 'd4': 5, 'f6': 3, 'g7': 2, 'h8': 1, 'd6': 6, 'f4': 4, 'b8': 5, 'c7': 3, 'g3': 1, 'h2': 2, 'a2': 6, 
# 'a7': 9, 'a8': 7, 'a3': 5, 'a6': 2, 'a4': 3, 'a5': 1, 'c2': 9, 'b3': 3, 'b1': 2, 'c1': 1, 'b9': 4, 'c9': 2, 'c8': 6, 'b7': 1, 'c4': 8, 'b5': 7, 'b6': 9, 'b4': 6, 
# 'c5': 5, 'c6': 4, 'd5': 8, 'f5': 2, 'd1': 9, 'd3': 4, 'd7': 7, 'd2': 1, 'd9': 3, 'd8': 2, 'e4': 1, 'e6': 7, 'e9': 5, 'e2': 3, 'e1': 8, 'e8': 4, 'e7': 6, 'e3': 2, 
# 'f3': 6, 'f1': 5, 'f2': 7, 'f7': 8, 'f8': 9, 'f9': 1, 'g1': 6, 'h1': 3, 'g2': 5, 'g6': 8, 'g8': 3, 'g5': 4, 'h5': 6, 'h6': 5, 'h7': 4, 'i2': 4, 'i5': 3, 'i6': 1, 
# 'i7': 5, 'i8': 8, 'i3': 9, 'h3': 8, 'i4': 2, 'g4': 7, 'g9': 9, 'h4': 9, 'h9': 7}
def set_input_values_with_solution_dict(solution_dict):
    for cell_id in solution_dict:
        set_input_value(cell_id, str(solution_dict[cell_id]))

# Puzzle: 
# [('a1', 4), ('a2', 6)]
def set_input_values_with_puzzle_list(puzzle):
    for cell_id, value in puzzle:
        set_input_value(cell_id, str(value))

def dict_to_list(d):
    return [(k, v) for k, v in d.items()]

def generate_puzzle_with_at_least_one_solution(amount=24, from_database=False):
    if not from_database:
        x, y, z = find_puzzle_with_at_least_one_solution(amount)
    else:
        x, y, z = find_puzzle_with_generate_puzzle_from_solution_data(amount, file_name=database_entry_line.get_text())
    print("Solution: ")
    print_solution(x)
    global solution
    solution = x
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)
    return y

def generate_puzzle_with_unique_solution(amount=24, from_database=False):
    if not from_database:
        x, y, z = find_puzzle_with_unique_solution(amount)
    else:
        x, y, z = find_puzzle_with_generate_puzzle_from_solution_data_with_unique_solution(amount, file_name=database_entry_line.get_text())
    print("Solution: ")
    print_solution(x)
    global solution
    solution = x
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)
    return y

def generate_puzzle_at_least_one_solution_with_given(list_of_cells, from_database=False):
    if not from_database:
        x, y, z = find_puzzle_with_given_cells_with_at_least_one_solution(list_of_cells)
    else:
        x, y, z = find_puzzle_with_generate_puzzle_from_solution_data_cells(list_of_cells, unique_solution=False, file_name=database_entry_line.get_text())
    print("Solution: ")
    print_solution(x)
    global solution
    solution = x
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)
    return y

def generate_puzzle_unique_solution_with_given(list_of_cells, from_database=False):
    if not from_database:
        x, y, z = find_puzzle_with_given_cells_with_unique_solution(list_of_cells)
    else:
        x, y, z = find_puzzle_with_generate_puzzle_from_solution_data_cells(list_of_cells, unique_solution=True, file_name=database_entry_line.get_text())
    print("Solution: ")
    print_solution(x)
    global solution
    solution = x
    print("\nPuzzle: ")
    print_puzzle(y) 
    print("\nAttempts: ")
    print(z)
    return y

# Buttons
amount_entry_line = pygame_gui.elements.UITextEntryLine(pygame.Rect((110, 700), (200, 40)),
                                                        ui_manager, placeholder_text="Amount : 27",
                                                        object_id=pygame_gui.core.ObjectID(class_id='@normal_text_entry_line',
                                                        object_id=''))
amount_entry_line.set_text_length_limit(2)
amount_entry_line.set_allowed_characters('numbers')
amount_entry_line.set_tooltip("Amount of given cells to be filled in the puzzle. Recommended amount is 27.")

given_entry_line = pygame_gui.elements.UITextEntryLine(pygame.Rect((700, 100), (400, 40)),
                                                        ui_manager, placeholder_text="['a1']",
                                                        object_id=pygame_gui.core.ObjectID(class_id='@normal_text_entry_line',
                                                        object_id=''))
given_entry_line.set_text("['a1', 'b2', 'c3', 'a4', 'b5', 'c6', 'a7', 'b8', 'c9', 'd1', 'e2', 'f3', 'd4', 'e5', 'f6', 'd7', 'e8', 'f9', 'g1', 'h2', 'i3', 'g4', 'h5', 'i6', 'g7', 'h8', 'i9']")
given_entry_line.set_text_length_limit(300)
given_entry_line.set_tooltip("List of cells to be given cells to be filled in the puzzle")

button5 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 150), (400, 40)),
                                      text='Generate with solution with given cells',
                                      manager=ui_manager,
                                      tool_tip_text = "Generate puzzle with at least 1 vaild solution")

button6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 200), (400, 40)),
                                      text='Generate with unique solution with given cells',
                                      manager=ui_manager,
                                      tool_tip_text = "Generate puzzle with a unique solution. Incorrect setup will take the program a long time to find a puzzle.")
button7 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 250), (400, 40)),
                                      text='Generate Symmetric Given Cells',
                                      manager=ui_manager,
                                      tool_tip_text = "Generate random list of symmetric given cells")


# Database entry line
database_entry_line = pygame_gui.elements.UITextEntryLine(pygame.Rect((700, 300), (400, 40)),
                                                        ui_manager, placeholder_text="Enter database name",
                                                        object_id=pygame_gui.core.ObjectID(class_id='@normal_text_entry_line',
                                                        object_id=''))
database_entry_line.set_text_length_limit(300)
database_entry_line.set_tooltip("The database used to generate puzzles.")
database_entry_line.set_text("solutions.txt")
# database_entry_line.get_text()

# Drop down menu
random_or_database_dropdown = pygame_gui.elements.UIDropDownMenu(["Generation Method : Random Fill", "Generation Method : Database"],
                                                        "Generation Method : Random Fill",
                                                        pygame.Rect((700, 350), (400, 35)),
                                                        ui_manager)
# random_or_database_dropdown.selected_option()

button6 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 700), (400, 40)),
                                      text='Show Solution',
                                      manager=ui_manager,
                                      tool_tip_text = "Show a solution for the current puzzle.")

button1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((340, 700), (300, 40)),
                                      text='Generate puzzle with solution',
                                      manager=ui_manager,
                                      tool_tip_text = "Generate puzzle with at least 1 vaild solution")

button2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 750), (540, 40)),
                                      text='Generate puzzle with a unique solution by random fill',
                                      manager=ui_manager,
                                      tool_tip_text = "Generate puzzle with a unique solution. Incorrect setup will take the program a long time to find a puzzle.")
button3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 650), (400, 40)),
                                      text='Clear Board',
                                      manager=ui_manager,
                                      tool_tip_text = "Clear Board")
button4 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 750), (400, 40)),
                                      text='Quit',
                                      manager=ui_manager,
                                      tool_tip_text = "Quit")

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element.text == "Generate puzzle with solution":
                reset_board()
                if random_or_database_dropdown.selected_option == "Generation Method : Random Fill":
                    if amount_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_with_at_least_one_solution(amount=27))
                    else:
                        set_input_values_with_puzzle_list(generate_puzzle_with_at_least_one_solution(int(amount_entry_line.get_text())))

                elif random_or_database_dropdown.selected_option == "Generation Method : Database":
                    if amount_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_with_at_least_one_solution(amount=27, from_database=True))
                    else:
                        set_input_values_with_puzzle_list(generate_puzzle_with_at_least_one_solution(int(amount_entry_line.get_text()), from_database=True))

            elif event.ui_element.text == "Generate puzzle with a unique solution by random fill":
                reset_board()
                if random_or_database_dropdown.selected_option == "Generation Method : Random Fill":
                    if amount_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_with_unique_solution(amount=27))
                    else:
                        set_input_values_with_puzzle_list(generate_puzzle_with_unique_solution(int(amount_entry_line.get_text())))

                elif random_or_database_dropdown.selected_option == "Generation Method : Database":
                    if amount_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_with_unique_solution(amount=27, from_database=True))
                    else:
                        set_input_values_with_puzzle_list(generate_puzzle_with_unique_solution(int(amount_entry_line.get_text()), from_database=True))

            elif event.ui_element.text == "Generate with solution with given cells":
                reset_board()
                if random_or_database_dropdown.selected_option == "Generation Method : Random Fill":
                    if given_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_at_least_one_solution_with_given(['a1', 'b2', 'c3', 'a4', 'b5', 'c6', 'a7', 'b8', 'c9', 'd1', 'e2', 'f3', 'd4', 'e5', 'f6', 'd7', 'e8', 'f9', 'g1', 'h2', 'i3', 'g4', 'h5', 'i6', 'g7', 'h8', 'i9']))
                    else:
                        try:
                            given_cells = eval(given_entry_line.get_text())
                            if isinstance(given_cells, list):
                                set_input_values_with_puzzle_list(generate_puzzle_at_least_one_solution_with_given(given_cells))
                        except Exception as e:
                            print(f"Invalid input: {e}")
                elif random_or_database_dropdown.selected_option == "Generation Method : Database":
                    if given_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_at_least_one_solution_with_given(['a1', 'b2', 'c3', 'a4', 'b5', 'c6', 'a7', 'b8', 'c9', 'd1', 'e2', 'f3', 'd4', 'e5', 'f6', 'd7', 'e8', 'f9', 'g1', 'h2', 'i3', 'g4', 'h5', 'i6', 'g7', 'h8', 'i9'], from_database=True))
                    else:
                        try:
                            given_cells = eval(given_entry_line.get_text())
                            if isinstance(given_cells, list):
                                set_input_values_with_puzzle_list(generate_puzzle_at_least_one_solution_with_given(given_cells, from_database=True))
                        except Exception as e:
                            print(f"Invalid input: {e}")

            elif event.ui_element.text == "Generate with unique solution with given cells":
                reset_board()
                if random_or_database_dropdown.selected_option == "Generation Method : Random Fill":
                    if given_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_unique_solution_with_given(['a1', 'b2', 'c3', 'a4', 'b5', 'c6', 'a7', 'b8', 'c9', 'd1', 'e2', 'f3', 'd4', 'e5', 'f6', 'd7', 'e8', 'f9', 'g1', 'h2', 'i3', 'g4', 'h5', 'i6', 'g7', 'h8', 'i9']))
                    else:
                        try:
                            given_cells = eval(given_entry_line.get_text())
                            if isinstance(given_cells, list):
                                set_input_values_with_puzzle_list(generate_puzzle_unique_solution_with_given(given_cells))
                        except Exception as e:
                            print(f"Invalid input: {e}")
                elif random_or_database_dropdown.selected_option == "Generation Method : Database":
                    if given_entry_line.get_text() == "":
                        set_input_values_with_puzzle_list(generate_puzzle_unique_solution_with_given(['a1', 'b2', 'c3', 'a4', 'b5', 'c6', 'a7', 'b8', 'c9', 'd1', 'e2', 'f3', 'd4', 'e5', 'f6', 'd7', 'e8', 'f9', 'g1', 'h2', 'i3', 'g4', 'h5', 'i6', 'g7', 'h8', 'i9'], from_database=True))
                    else:
                        try:
                            given_cells = eval(given_entry_line.get_text())
                            if isinstance(given_cells, list):
                                set_input_values_with_puzzle_list(generate_puzzle_unique_solution_with_given(given_cells, from_database=True))
                        except Exception as e:
                            print(f"Invalid input: {e}")
            elif event.ui_element.text == "Generate Symmetric Given Cells":
                if amount_entry_line.get_text() == "":
                    amount = 13
                else:
                    amount = int(amount_entry_line.get_text()) * 0.5
                    amount = int(amount)
                given_entry_line.set_text(str(generate_symmetric_pattern_random(amount)))
            elif event.ui_element.text == "Clear Board":
                reset_board()
                solution = {}

            elif event.ui_element.text == "Show Solution":
                reset_board()
                set_input_values_with_solution_dict(solution)

            elif event.ui_element.text == "Quit":
                is_running = False
        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    ui_manager.draw_ui(window_surface)

    pygame.display.update()


