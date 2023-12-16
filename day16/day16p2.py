from day16p1 import Light, get_input, prep_solve, solve


def solve2(mirror_map):
    maximum_visited = 0
    max_row, max_col = Light.pos_limits

    # Top edge and Bottom edge
    for i in range(max_col + 1):
        prep_solve(mirror_map)
        s_light = Light((0, i), 2)
        curr_visited = solve(mirror_map, s_light)
        if curr_visited > maximum_visited:
            maximum_visited = curr_visited

        prep_solve(mirror_map)
        s_light = Light((max_row, i), 0)
        curr_visited = solve(mirror_map, s_light)
        if curr_visited > maximum_visited:
            maximum_visited = curr_visited
    # Left edge and Right edge
    for i in range(max_row + 1):
        prep_solve(mirror_map)
        s_light = Light((i, 0), 1)
        curr_visited = solve(mirror_map, s_light)
        if curr_visited > maximum_visited:
            maximum_visited = curr_visited

        prep_solve(mirror_map)
        s_light = Light((i, max_col), 3)
        curr_visited = solve(mirror_map, s_light)
        if curr_visited > maximum_visited:
            maximum_visited = curr_visited

    return maximum_visited


if __name__ == "__main__":
    m_map = get_input("day16.txt")

    prep_solve(m_map)
    print(solve2(m_map))
