import copy


def get_input(file_location):
    galaxy_map = []
    with (open(file_location, "r") as file):
        curr_row = file.readline().strip()
        while curr_row != "":
            galaxy_map.append(list(curr_row))
            curr_row = file.readline().strip()
    return galaxy_map


def cosmic_expansion(galaxy_map: list):
    # I don't need forgiveness for the following code.
    # I don't even forgive myself for that

    new_galaxy_map = []
    # Row expansion
    row_expansion = []
    for i, row in enumerate(galaxy_map):
        if "#" in row:
            continue
        else:
            row_expansion.append(i)
    empty_row = ["M"] * len(galaxy_map[0])
    for i, row in enumerate(galaxy_map):
        new_galaxy_map.append(row)
        if i in row_expansion:
            new_galaxy_map.append(empty_row)
    # Swap
    galaxy_map = copy.deepcopy(new_galaxy_map)
    new_galaxy_map = []
    # Col expansion
    col_expansion = []
    for i, _ in enumerate(galaxy_map[0]):
        col = [galaxy_map[x][i] for x in range(len(galaxy_map))]
        if "#" in col:
            continue
        else:
            col_expansion.append(i)
    for i, row in enumerate(galaxy_map):
        new_galaxy_map.append([])
        for j, col in enumerate(galaxy_map[i]):
            new_galaxy_map[i].append(col)
            if j in col_expansion:
                new_galaxy_map[i].append("M")

    return new_galaxy_map


def get_galaxies_pos(galaxy_map):
    galaxies = []
    for row, line in enumerate(galaxy_map):
        for col, value in enumerate(line):
            if value == "#":
                galaxies.append((row, col))
    return galaxies


def solve(galaxy_map):
    result = 0
    galaxies = get_galaxies_pos(galaxy_map)
    for i, galaxy in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            other_galaxy = galaxies[j]
            result += (
                abs(galaxy[0] - other_galaxy[0]) +
                abs(galaxy[1] - other_galaxy[1])
            )

    return result


if __name__ == "__main__":
    g_map = get_input("day11.txt")
    g_map = cosmic_expansion(g_map)
    # print(*g_map, sep="\n")
    print(solve(g_map))
