from day22p1 import *


def solve2(brick_list):
    result = 0

    new_brick_list, occupied_pos = simulate_bricks(brick_list)
    new_brick_list.sort()

    for brick in new_brick_list:
        new_new_brick_list = copy.deepcopy(new_brick_list)
        new_new_brick_list.remove(brick)

        result += simulate_bricks_reaction(new_new_brick_list)

    return result


def simulate_bricks_reaction(brick_list):
    brick_fall_count = 0
    occupied_pos = set()

    for brick_z, brick_start, brick_end in brick_list:
        fall_once = False
        while True:
            brick_pos = expand_brick(brick_start, brick_end)
            if brick_z == 1:
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
                if not fall_once:
                    fall_once = True
                    brick_fall_count += 1
            else:

                occupied_pos.update(brick_pos)
                break

    return brick_fall_count


if __name__ == "__main__":
    b_list = get_input("day22.txt")
    print(f">>> {solve2(b_list)}")
