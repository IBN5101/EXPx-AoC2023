from day11p1 import *


def solve2(galaxy_map):
    result = 0
    galaxies = get_galaxies_pos(galaxy_map)
    for i, galaxy in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            other_galaxy = galaxies[j]
            # Set up
            curr_row, curr_col = galaxy
            goto_row, goto_col = other_galaxy

            # Since the get_galaxy_pos function scan
            # for each row, then left to right,
            # that means the order of the stars will always be
            # top to bottom, then left to right.

            # Go down
            while curr_row != goto_row:
                curr_row += 1
                if galaxy_map[curr_row][curr_col] == "M":
                    result += 1000000 - 1
                else:
                    result += 1
            # Go left or right
            increment = 1 if curr_col < goto_col else -1
            while curr_col != goto_col:
                curr_col += increment
                if galaxy_map[curr_row][curr_col] == "M":
                    result += 1000000 - 1
                else:
                    result += 1

    return result


if __name__ == "__main__":
    g_map = get_input("day11.txt")
    g_map = cosmic_expansion(g_map)
    # print(*g_map, sep="\n")
    print(solve2(g_map))
