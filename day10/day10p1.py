import math


# Direction array:
# 0 = North
# 1 = East
# 2 = South
# 3 = West

def get_input(file_location):
    i_map = []
    s_pos = []
    with (open(file_location, "r") as file):
        curr_line = file.readline()
        while curr_line != "" and curr_line != "\n":
            curr_row = list(curr_line.strip())
            i_map.append(curr_row)

            curr_line = file.readline()

    for i, curr_row in enumerate(i_map):
        if "S" in curr_row:
            s_pos = [i, curr_row.index("S")]
            break

    return i_map, s_pos


def print_input(i_map, s_pos):
    for curr_row in i_map:
        print(curr_row)
    print(s_pos)


def symbol_to_directions(sym):
    if sym == "|":
        return [True, False, True, False]
    elif sym == "-":
        return [False, True, False, True]
    elif sym == "L":
        return [True, True, False, False]
    elif sym == "J":
        return [True, False, False, True]
    elif sym == "7":
        return [False, False, True, True]
    elif sym == "F":
        return [False, True, True, False]
    elif sym == ".":
        return [False, False, False, False]
    elif sym == "S":
        return [True, True, True, True]
    else:
        raise Exception("No symbol found")


def go_to_next_pos(curr_pos, direction):
    cy, cx = curr_pos
    if direction == 0:
        return [cy - 1, cx]
    elif direction == 1:
        return [cy, cx + 1]
    elif direction == 2:
        return [cy + 1, cx]
    elif direction == 3:
        return [cy, cx - 1]
    else:
        raise Exception("Invalid direction!")


def solve_map(i_map, s_pos):
    # 1. From starting position, iterate from North and go clockwise.
    # 2. Initialize step and current direction.
    # 3. Pick next block from current direction.
    # 4. If next block is invalid, continue step 1.
    # 5. If next block is "S", break out of step 1.
    # 6. Obtain the directions of next block.
    # 7. For the next block to be valid,
    # the opposite of current direction must return True
    # 8. If next block is valid, update current direction. Else continue step 1.

    for starting_direction in range(4):
        # print(">>>" + str(starting_direction))
        steps = 0
        curr_direction = starting_direction
        curr_pos = s_pos

        while True:
            next_pos = go_to_next_pos(curr_pos, curr_direction)
            next_y, next_x = next_pos
            if not (0 <= next_y < len(i_map)):
                break
            if not (0 <= next_x < len(i_map[0])):
                break

            next_symbol = i_map[next_y][next_x]
            if next_symbol == "S":
                return math.ceil(steps / 2)

            # print(next_symbol)

            next_directions = symbol_to_directions(next_symbol)
            if not next_directions[(curr_direction + 2) % 4]:
                break

            for i, direction in enumerate(next_directions):
                if i == ((curr_direction + 2) % 4):
                    continue
                elif direction:
                    curr_direction = i
                    curr_pos = next_pos
                    steps += 1
                    break

    return 0


if __name__ == "__main__":
    input_map, start_pos = get_input("day10.txt")
    # print_input(input_map, start_pos)
    print(solve_map(input_map, start_pos))
