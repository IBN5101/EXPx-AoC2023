def get_input(file_location):
    input_array = []
    with (open(file_location, "r") as file):
        curr_line = file.readline().strip()
        while curr_line != "":
            input_array.append(list(curr_line))
            curr_line = file.readline().strip()

    return input_array


def get_all_adjacent_cells(curr_row, number_start, number_end):
    cell_list = []
    for row in range(curr_row - 1, curr_row + 2):
        cell_list.append((row, number_start - 1))
        cell_list.append((row, number_end + 1))
    for col in range(number_start, number_end + 1):
        cell_list.append((curr_row - 1, col))
        cell_list.append((curr_row + 1, col))
    return cell_list


def filter_cell_list(cell_list, input_array):
    new_cell_list = []

    row_max = len(input_array) - 1
    col_max = len(input_array[0]) - 1

    for cell in cell_list:
        row, col = cell
        if not (0 <= row <= row_max):
            continue
        if not (0 <= col <= col_max):
            continue
        new_cell_list.append(cell)
    return new_cell_list


def detect_symbol(cell_list, input_array):
    for cell in cell_list:
        row, col = cell
        content = input_array[row][col]
        if content.isdigit():
            continue
        if content == ".":
            continue
        return True
    return False


def solve(input_array: list):
    result = 0
    valid_number_list = []
    for row, line in enumerate(input_array):
        is_number_start = False
        is_number_end = False
        number_start = 0
        number_end = 0

        index = 0
        while index < len(line):
            # Digit is found
            if line[index].isdigit():
                # New number group
                if not is_number_start:
                    is_number_start = True
                    number_start = index
                # Edge case: number at end of line
                if index == len(line) - 1:
                    is_number_end = True
                    number_end = index
            # Symbol is found
            else:
                # End of number group
                if is_number_start:
                    is_number_end = True
                    number_end = index - 1

            # Process number group
            if is_number_end:
                adj_cells = get_all_adjacent_cells(row, number_start, number_end)
                adj_cells = filter_cell_list(adj_cells, input_array)
                symbol_found = detect_symbol(adj_cells, input_array)

                # Number group is adjacent to symbol
                if symbol_found:
                    curr_number = 0
                    for i in range(number_start, number_end + 1):
                        curr_number = curr_number * 10 + int(line[i])
                    result += curr_number

                    number_data = [row, number_start, number_end, curr_number]
                    valid_number_list.append(number_data)

                # Reset variables
                is_number_start = False
                is_number_end = False
                number_start = 0
                number_end = 0

            index += 1

    return result, valid_number_list


if __name__ == "__main__":
    i_array = get_input("day03.txt")
    # print(*i_array, sep="\n")
    print(solve(i_array)[0])
