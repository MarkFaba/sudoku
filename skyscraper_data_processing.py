data_example = {'a1': 8, 'a5': 6, 'a6': 7, 'a8': 5, 'b2': 2, 'b6': 4, 'b8': 6, 'c4': 5, 'c5': 3, 'c7': 4, 'c8': 8, 'd7': 9, 'e7': 5, 'e8': 2, 'f1': 9, 'f2': 7, 'f8': 4, 'g1': 2, 'h2': 5, 'h3': 3, 'h7': 2, 'i4': 3, 'i5': 9, 'i8': 1, 'a7': 3, 'b5': 8, 'b4': 9, 'a4': 2, 'c6': 1, 'a9': 9, 'a2': 4, 'a3': 1, 'b3': 5, 'b1': 3, 'b7': 7, 'b9': 1, 'c9': 2, 'c1': 7, 'c2': 9, 'c3': 6, 'd8': 7, 'h8': 9, 'g8': 3, 'e3': 8, 'f3': 2, 'd3': 4, 'i3': 7, 'g3': 9, 'e1': 6, 'e9': 3, 'e2': 1, 'd1': 5, 'd2': 3, 'e6': 9, 'i1': 4, 'h1': 1, 'd5': 2, 'd6': 8, 'd9': 6, 'd4': 1, 'f4': 6, 'f5': 5, 'f6': 3, 'f9': 8, 'f7': 1, 'h6': 6, 'g6': 5, 'i6': 2, 'i9': 5, 'e4': 7, 'e5': 4, 'h5': 7, 'g5': 1, 'h9': 4, 'g9': 7, 'h4': 8, 'g4': 4, 'g2': 8, 'g7': 6, 'i2': 6, 'i7': 8}

row_a = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']
row_a_reversed = ['a9', 'a8', 'a7', 'a6', 'a5', 'a4', 'a3', 'a2', 'a1']
column_1 = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1']
column_1_reversed = ['i1', 'h1', 'g1', 'f1', 'e1', 'd1', 'c1', 'b1', 'a1']

# Working correctly
def get_row_key(data, row_index, reversed_order=False, sort=False) -> list:
    """
    Get row key from data

    :param data: dict
    :param row_index: str
    :param reversed_order: bool
    :param sort: bool
    :return: list
    """
    row = [key for key in data.keys() if key[0] == row_index]
    if reversed_order:
        row = sorted(row, reverse=True)
    elif sort:
        row = sorted(row)
    return row

def get_column_key(data, column_index, reversed_order=False, sort=False) -> list:
    """
    Get column key from data

    :param data: dict
    :param column_index: str
    :param reversed_order: bool
    :param sort: bool
    :return: list
    """
    column = [key for key in data.keys() if key[1] == column_index]
    if reversed_order:
        column = sorted(column, reverse=True)
    elif sort:
        column = sorted(column)
    return column

# print(get_column_key(data_example, '1', reversed_order=True, sort=True))

def get_value_from_keys_of_data(data, keys) -> list:
    """
    Get values from keys of data

    :param data: dict
    :param keys: list
    :return: list
    """
    values = []
    for key in keys:
        values.append(data[key])
    return values

# skyscraper_data = {'a': 0, 'b': 0, ..., 'a_r': 0, 'b_r': 0, ..., '1': 0, '2': 0, ..., '1_r': 0, '2_r': 0, ...}
def init_skyscraper_data() -> dict:
    """
    Init skyscraper data

    :param data: dict
    :return: dict
    """
    skyscraper_data = {}
    for i in range(1, 10):
        skyscraper_data[str(i)] = 0
        skyscraper_data[str(i) + '_r'] = 0
        skyscraper_data[chr(i + 96)] = 0
        skyscraper_data[chr(i + 96) + '_r'] = 0
    return skyscraper_data


"""
update data: 

skyscraper_list_a = get_value_from_keys_of_data(one_line_of_data, get_row_key(one_line_of_data, 'a', sort=True))
skyscraper_x(skyscraper_list_a) -> value
skyscraper_data['a'] = value

skyscraper_list_b = get_value_from_keys_of_data(one_line_of_data, get_row_key(one_line_of_data, 'b', sort=True))
skyscraper_x(skyscraper_list_b) -> value
skyscraper_data['b'] = value

...

skyscraper_list_a_r = get_value_from_keys_of_data(one_line_of_data, get_row_key(one_line_of_data, 'a', reversed_order=True, sort=True))
skyscraper_x(skyscraper_list_a_r) -> value
skyscraper_data['a_r'] = value

...

skyscraper_list_1 = get_value_from_keys_of_data(one_line_of_data, get_column_key(one_line_of_data, '1', sort=True))
skyscraper_x(skyscraper_list_1) -> value
skyscraper_data['1'] = value

"""
def skyscraper_x(y):
    x = 0  
    max_seen = 0  
    for i in y:  
        if i > max_seen:  
            x += 1  
            max_seen = i  
    return x  

def update_skyscraper_data(skyscraper_data, data):
    for i in range(1, 10):
        row_index = chr(i + 96)
        column_index = str(i)

        # get the list of values for each row and column
        row_keys = get_row_key(data, row_index, sort=True)
        row_values = get_value_from_keys_of_data(data, row_keys)

        column_keys = get_column_key(data, column_index, sort=True)
        column_values = get_value_from_keys_of_data(data, column_keys)

        # count the number of skyscrapers that can be seen
        skyscraper_data[row_index] = skyscraper_x(row_values)
        skyscraper_data[column_index] = skyscraper_x(column_values)

        # repeat the same for reversed order
        row_keys_reversed = get_row_key(data, row_index, reversed_order=True, sort=True)
        row_values_reversed = get_value_from_keys_of_data(data, row_keys_reversed)

        column_keys_reversed = get_column_key(data, column_index, reversed_order=True, sort=True)
        column_values_reversed = get_value_from_keys_of_data(data, column_keys_reversed)

        skyscraper_data[row_index + '_r'] = skyscraper_x(row_values_reversed)
        skyscraper_data[column_index + '_r'] = skyscraper_x(column_values_reversed)


# skyscraper_data = init_skyscraper_data()
# update_skyscraper_data(skyscraper_data, data_example)
# print(skyscraper_data)

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

# print_solution(data_example)

# return certain line of the solutions file, should be a dict
def get_log_file_line(line_number):
    with open("solutions.txt", "r") as f:
        lines = f.readlines()
        return eval(lines[line_number - 1])

# Write skyscraper_data dict as 1 line to skyscraper.txt.
def write_skyscraper_data_to_file(skyscraper_data):
    if skyscraper_data is not {}:
        with open("solutions_skyscraper_data.txt", "a") as f:
            f.write(str(skyscraper_data) + "\n")

# loop through solutions.txt for data_example, update skyscraper_data, and write to solutions_skyscraper_data.txt
def update_skyscraper_data_from_solutions_file(lines):
    for i in range(1, lines + 1):
        skyscraper_data = init_skyscraper_data()
        solution_dict = get_log_file_line(i)
        if solution_dict is not None:
            update_skyscraper_data(skyscraper_data, solution_dict)
            write_skyscraper_data_to_file(skyscraper_data)
        else:
            raise Exception
        
update_skyscraper_data_from_solutions_file(13685)
