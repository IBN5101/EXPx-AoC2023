from day03p1 import *


def get_all_adj_stars(cell_list, input_array):
    star_list = []
    for cell in cell_list:
        row, col = cell
        content = input_array[row][col]
        if content == "*":
            star_list.append(cell)
    return star_list


def solve2(valid_number_list, input_array):
    result = 0
    star_map = dict()
    for number_data in valid_number_list:
        row, number_start, number_end, curr_number = number_data
        adj_cells = get_all_adjacent_cells(row, number_start, number_end)
        adj_cells = filter_cell_list(adj_cells, input_array)
        adj_cells = get_all_adj_stars(adj_cells, input_array)
        # Number is adjacent to a "*"
        for cell in adj_cells:
            if cell not in star_map:
                star_map[cell] = [curr_number]
            else:
                star_map[cell].append(curr_number)

    for number_list in star_map.values():
        if len(number_list) == 2:
            result += number_list[0] * number_list[1]

    return result


if __name__ == "__main__":
    i_array = get_input("day03.txt")
    v_number_list = solve(i_array)[1]
    print(solve2(v_number_list, i_array))
