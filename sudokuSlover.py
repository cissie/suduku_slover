__author__ = 'student'
import math


def enterpuzzle(puzzle):
    while True:
        # puzzle = raw_input('please enter your 81 digit puzzle use "." for blank spots :\n')
        # Validate that user input is len = 81
        if not len(puzzle) == 81:
            print("please enter a value that is equal to 81 charactors long. Please try again")
            continue
        #Validate that user input only has numbers or .
        valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
        for char in puzzle:
            if not char in valid:
                print(char + " is not a valid value please reenter puzzle without using " + char)
        break


def display(puzzle):
    display = ''
    ii = 0
    for char in puzzle:
        # format first line
        if ii % 81 == 0:
            display = "+---+---+---+\n|" + char
        # format rows
        elif ii % 27 == 0:
            display = display + "|\n+---+---+---+\n|" + char
        # format last column
        elif ii % 9 == 0:
            display = display + "|\n|" + char
        # format columns
        elif ii % 3 == 0:
            display = display + "|" + char
        # insert nonformated data
        else:
            display = display + char
        ii += 1

    display = display + "|\n+---+---+---+"

    print(display)


def find_row(numbervalue):
    row = numbervalue / 9
    row = math.floor(row)
    row = int(row)
    return row
    # given any position in the puzzle this will return the row


def find_column(numbervalue):
    column = numbervalue % 9
    column = int(column)
    return column
    return
    # given any position in the puzzle this will return the column


def find_box(numbervalue):
    # finds the box that a given cell belongs to e.g. start with upper left 0
    row = find_row(numbervalue)
    row = row / 3
    row = math.floor(row)

    column = find_column(numbervalue)
    column = column / 3
    column = math.floor(column)

    box_number = column + row * 3
    box_number = int(box_number)
    return box_number
    # given any position in the puzzle this will return the boxNumber


def cell_current_properties():
    return


def check_for_available_values(cell_index):
    return


def get_all_indexs_for_row(row):
    indexs = []
    for x in range(0, 9):
        next_index = x + 9 * row
        indexs.append(next_index)
    return indexs


def get_all_indexs_for_column(column):
    """
    given any index in the puzzle this returns a list of indexs in that column
    :param column: column number
    :return: indexs[]
    """
    indexs = []
    for x in range(0, 9):
        next_index = x * 9 + column
        indexs.append(next_index)
    return indexs


def get_all_indexs_for_box(box):
    """
    given any index in the puzzle this returns a list of indexs in that box
    :param box: box number
    :return: indexs[]
    """
    row = box / 3
    row = int(math.floor(row))
    row = row * 27

    column = box % 3
    column = int(math.floor(column))
    column = column * 3
    indexs = []
    for x in range(0, 3):
        for y in range(0, 3):
            next_index = x * 9 + y + column + row
            indexs.append(next_index)
    return indexs


def get_all_indexs_related_cell(index):
    related_cells = []
    box = find_box(index)
    box = get_all_indexs_for_box(box)
    related_cells.extend(box)
    column = find_column(index)
    column = get_all_indexs_for_column(column)
    related_cells.extend(column)
    row = find_row(index)
    row = get_all_indexs_for_row(row)
    related_cells.extend(row)
    related_cells = set(related_cells)
    related_cells = list(related_cells)
    return related_cells


def get_possable_locations_for_number(unsloved_list, puzzle, value):
    possable_locations = []
    # loop though each unsloved value
    for orgain_cell in unsloved_list:
        possable = can_cell_be_value(puzzle, value, orgain_cell)
        if possable:
            possable_locations.append(orgain_cell)


    return possable_locations

    # active_column = find_column(cell)
    #active_box = find_box(cell)
    return


def get_unsloved_cells(puzzle):
    unsloved = []
    ii = 0
    for char in puzzle:
        if char == ".":
            unsloved.append(ii)
        ii += 1
    # returns unsloved index
    return unsloved


def get_number_values(cell_index_list, puzzle):
    # given a list of cell indexs returns a list of the values contained
    values = []
    for index in cell_index_list:
        if not puzzle[index] == ".":
            value = puzzle[index]
            values.append(value)
    return values


def can_cell_be_value(puzzle, value, cell):
    related_cells = get_all_indexs_related_cell(cell)
    for related_cell in related_cells:
        cell_puzzle_value = puzzle[related_cell]
        if cell_puzzle_value ==  '.':
            continue
        if value == int(cell_puzzle_value):
            return False
    return True


def search_for_only_in_row(possable_locations):
    for ii in range(9):
        row = get_all_indexs_for_row(ii)
        valid_index_for_row = set(possable_locations) & set(row)
        if len(valid_index_for_row) == 1:
            print ("you found a value for index " + str(valid_index_for_row))
        print (valid_index_for_row)
def search_for_only_in_box(possable_locations):
    for ii in range(9):
        column = get_all_indexs_for_column(ii)
        valid_index_for_box = set(possable_locations) & set(box)
        if len(valid_index_for_box) == 1:
            print ("you found a value for index " + str(valid_index_for_box))
        print (valid_index_for_box)
def search_for_only_in_column(possable_locations):
    for ii in range(9):
        column = get_all_indexs_for_column(ii)
        valid_index_for_column = set(possable_locations) & set(column)
        if len(valid_index_for_column) == 1:
            print ("you found a value for index " + str(valid_index_for_column))
        print (valid_index_for_column)

def search_for_only_in_area(possable_locations,):
    area = []
    sloved_locations = []
    for ii in range(9):
        row = get_all_indexs_for_row(ii)
        column = get_all_indexs_for_column(ii)
        box = get_all_indexs_for_box(ii)
        area.append(row)
        area.append(column)
        area.append(box)
    for list in area:
        valid_values_for_area = set(possable_locations) & set(list)
        if len(valid_values_for_area) == 1:
            print ("you found a value for index " + str(valid_values_for_area) + 'in area ' + str(list))
            sloved_locations.append(valid_values_for_area)
        print (set(valid_values_for_area))
    # this is to remove duplicates
    sloved_locations = uniq(sloved_locations)
    return sloved_locations

def uniq(input):
## used to remove non unique items
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

puzzle = '..9.43..........3.41..7.............8..5...6..4...6..2.......1...4.98..67..6..52.'
enterpuzzle(puzzle)

unsloved = get_unsloved_cells(puzzle)
value = 3
#get_possable_locations_for_number(unsloved, puzzle, value)
print(get_all_indexs_related_cell(0))
display(puzzle)
possable_locations = get_possable_locations_for_number(unsloved, puzzle, value)

print (search_for_only_in_area(possable_locations))


#print (can_cell_be_value(puzzle,2,0))
#print (can_cell_be_value(puzzle,9,0))
#display(puzzle)
#give me a puzzle
#for this puzzle give me all that place that can be 1
#look at the first place that can be 1
#can any other value in this row be 1?
#can any other value in this colomn be 1?
#can any other value in this box ?
#if so change len[index] to 1