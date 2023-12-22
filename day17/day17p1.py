# 2D array: (row, col)
# row: top to bottom, col: left to right
import copy


def get_input(file_location):
    maze_map = []
    with (open(file_location, "r") as file):
        curr_row = file.readline()
        while curr_row != "":
            curr_row = list(curr_row.strip())
            curr_row = list(map(int, curr_row))
            maze_map.append(curr_row)
            curr_row = file.readline()
    return maze_map


class Pointer:
    # DIRECTION: Up, Right, Down, Left
    DIRECTION = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]
    MAZE_MAP = []
    MAZE_END = (0, 0)

    def __init__(self, starting_pos):
        self.pos = starting_pos
        self.direction = None
        self.straight_line_check = []
        self.g_value = 0
        self.h_value = self.heuristic(self.pos)
        self.value = self.g_value + self.h_value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def move(self, new_pos):
        curr_row, curr_col = self.pos
        new_row, new_col = new_pos
        new_direction = (new_row - curr_row, new_col - curr_col)

        if new_pos == self.pos:
            raise Exception("Next pos is not moving.")
        if new_direction not in Pointer.DIRECTION:
            raise Exception("Invalid direction.")

        if len(self.straight_line_check) == 0 or \
                self.straight_line_check[0] == new_direction:
            self.straight_line_check.append(new_direction)
        else:
            self.straight_line_check = [new_direction]

        self.pos = new_pos
        self.direction = new_direction

        self.g_value += Pointer.MAZE_MAP[new_row][new_col]
        self.h_value = self.heuristic(self.pos)
        self.value = self.g_value + self.h_value

    def choice(self):
        choices = []
        if self.direction is None:
            for direction in Pointer.DIRECTION:
                next_pos = self.add_pos(self.pos, direction)
                choices.append(next_pos)
        else:
            dir_forward = Pointer.DIRECTION.index(self.direction)
            for i in range(-1, 2):
                next_pos = self.add_pos(
                    self.pos,
                    Pointer.DIRECTION[(dir_forward + i) % 4])
                choices.append(next_pos)

            if len(self.straight_line_check) >= 3:
                choices.pop(1)

        choices = [x for x in choices if self.valid_pos(x)]
        return choices

    @staticmethod
    def valid_pos(pos):
        row, col = pos
        if not (0 <= row < len(Pointer.MAZE_MAP)):
            return False
        if not (0 <= col < len(Pointer.MAZE_MAP[0])):
            return False
        return True

    @staticmethod
    def add_pos(pos1, pos2):
        return tuple(map(sum, zip(pos1, pos2)))

    @staticmethod
    def check_heat_loss(pos):
        return Pointer.MAZE_MAP[pos[0]][pos[1]]

    @staticmethod
    def heuristic(pos):
        row, col = pos
        end_row, end_col = Pointer.MAZE_END
        h = (end_row - row) + (end_col - col)
        return h * 0


def solve_dijkstra(maze_map):
    result = 999
    Pointer.MAZE_MAP = maze_map
    Pointer.MAZE_END = (len(maze_map) - 1, len(maze_map[0]) - 1)

    open_list = [Pointer((0, 0))]
    closed_list = set()
    value_so_far = dict()
    value_so_far[open_list[0].pos] = 0

    steps = 0

    while True:
        pointer = open_list.pop()

        # Credit to HyperNeutrino:
        # - Link: https://youtu.be/2pDSooPLLkI
        check = (pointer.pos, pointer.direction, len(pointer.straight_line_check))
        if check in closed_list:
            continue
        closed_list.add(check)

        if pointer.pos == Pointer.MAZE_END:
            result = pointer.g_value
            break

        choices = pointer.choice()
        # choices = [x for x in choices if x not in closed_list]

        for choice in choices:
            new_pointer = copy.deepcopy(pointer)
            new_pointer.move(choice)
            do_append = True
            # if new_pointer.pos in value_so_far and \
            #         new_pointer.value > value_so_far[new_pointer.pos]:
            #     do_append = False
            if do_append:
                value_so_far[new_pointer.pos] = new_pointer.value
                open_list.append(new_pointer)

        steps += 1

        if steps % 1 == 0:
            open_list.sort(reverse=True)
        if steps % 1000 == 0:
            print(pointer.pos, pointer.g_value, pointer.h_value, len(open_list))

    # print_map_annotated(maze_map, list(closed_list))
    return result


def print_map_annotated(maze_map: list, pos_list: list, pos1: tuple = None):
    new_maze_map = copy.deepcopy(maze_map)
    for pos in pos_list:
        new_maze_map[pos[0]][pos[1]] = "#"
    if pos1 is not None:
        new_maze_map[pos1[0]][pos1[1]] = "."

    for row in new_maze_map:
        for value in row:
            print(value, end="")
        print()


if __name__ == "__main__":
    m_map = get_input("day17.txt")
    print(solve_dijkstra(m_map))
