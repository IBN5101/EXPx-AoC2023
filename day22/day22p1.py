import copy


def get_input(file_location):
    brick_list = []
    with (open(file_location, "r") as file):
        curr_row = file.readline().strip()
        while curr_row != "":
            curr_row = curr_row.split("~")
            brick_start, brick_end = [x.split(",") for x in curr_row]

            brick_start = tuple(map(int, brick_start))
            brick_end = tuple(map(int, brick_end))
            brick_z = brick_start[2]
            brick_list.append([brick_z, brick_start, brick_end])

            curr_row = file.readline().strip()
    brick_list.sort()
    return brick_list


def solve(brick_list):
    result = 0

    new_brick_list, occupied_pos = simulate_bricks(brick_list)
    new_brick_list.sort()
    # print_test_data(occupied_pos)
    # print(*new_brick_list, sep="\n")

    height_dict = dict()
    for brick_z, brick_start, brick_end in new_brick_list:
        if brick_z in height_dict:
            height_dict[brick_z].append([brick_z, brick_start, brick_end])
        else:
            height_dict[brick_z] = [[brick_z, brick_start, brick_end]]

    for brick_z, brick_start, brick_end in new_brick_list:
        deleted_pos = tuple(expand_brick(brick_start, brick_end))

        bricks_to_test = []
        z_end = brick_end[2]
        for i in range(brick_z + 1, z_end + 2):
            if i in height_dict:
                bricks_to_test.extend(height_dict[i])
        can_fall = simulate_brick_deletion(
            bricks_to_test,
            deleted_pos,
            occupied_pos
        )
        result += 0 if can_fall else 1

    return result


def simulate_bricks(brick_list):
    new_brick_list = []
    occupied_pos = set()

    for brick_z, brick_start, brick_end in brick_list:
        while True:
            brick_pos = expand_brick(brick_start, brick_end)
            if brick_z == 1:
                new_brick_list.append([brick_z, brick_start, brick_end])
                occupied_pos.update(brick_pos)
                break

            can_fall = True
            for pos in brick_pos:
                pos_below = get_pos_below(pos)
                if pos_below in occupied_pos:
                    can_fall = False
                    break

            if can_fall:
                brick_z -= 1
                brick_start = get_pos_below(brick_start)
                brick_end = get_pos_below(brick_end)
            else:
                new_brick_list.append([brick_z, brick_start, brick_end])
                occupied_pos.update(brick_pos)
                break

    return new_brick_list, occupied_pos


def print_test_data(occupied_pos):
    print_x = []
    print_y = []
    for i in range(8):
        print_x.append(copy.deepcopy([".", ".", "."]))
        print_y.append(copy.deepcopy([".", ".", "."]))
    for pos in occupied_pos:
        x, y, z = pos

        x_target = print_x[z][x]
        if x_target == ".":
            print_x[z][x] = "/"
        else:
            print_x[z][x] = "#"

        y_target = print_y[z][y]
        if y_target == ".":
            print_y[z][y] = "/"
        else:
            print_y[z][y] = "#"
    print_x.reverse()
    print_y.reverse()

    print(*print_x, sep="\n")
    print()
    print(*print_y, sep="\n")
    # print(*occupied_pos)


def simulate_brick_deletion(bricks_to_test, deleted_pos, occupied_pos):
    for brick_z, brick_start, brick_end in bricks_to_test:
        brick_pos = tuple(expand_brick(brick_start, brick_end))
        can_fall = True
        for pos in brick_pos:
            pos_below = get_pos_below(pos)
            if pos_below in brick_pos:
                continue
            if pos_below in deleted_pos:
                continue
            if pos_below in occupied_pos:
                can_fall = False
                break
        if can_fall:
            return True

    return False


def get_pos_below(pos: tuple) -> tuple:
    return pos[0], pos[1], pos[2] - 1


def expand_brick(brick_start: tuple, brick_end: tuple) -> list[tuple]:
    pos_list = []

    # increment = (0, 0, 0)
    if brick_start[0] < brick_end[0]:
        increment = (1, 0, 0)
    elif brick_start[1] < brick_end[1]:
        increment = (0, 1, 0)
    elif brick_start[2] < brick_end[2]:
        increment = (0, 0, 1)
    elif brick_start == brick_end:
        return [brick_start]
    else:
        raise Exception("Invalid brick format.")

    i = 0
    while True:
        curr_pos = tuple([brick_start[j] + increment[j] * i for j in range(3)])
        pos_list.append(curr_pos)

        if curr_pos == brick_end:
            break
        i += 1

    return pos_list


if __name__ == "__main__":
    b_list = get_input("day22.txt")
    # print(*b_list, sep="\n")
    print(f">>> {solve(b_list)}")
