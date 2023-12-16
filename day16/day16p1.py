# Row goes down from top to bottom
# Col goes right from left to right
# pos = [Row, Col]
# Directions: clockwise starting from "up"
# 0 = up
# 1 = right
# 2 = down
# 3 = left

def get_input(file_location):
    mirror_map = []
    with (open(file_location, "r") as file):
        curr_row = file.readline()
        while curr_row != "":
            mirror_map.append(list(curr_row.strip()))
            curr_row = file.readline()
    return mirror_map


class Light:
    # Position constraints = bottom right position
    pos_limits = []
    # Visited set
    visited_set = set()
    # Splitter set
    splitter_set = set()

    def __init__(self, pos: tuple, direction: int):
        self.pos = pos
        self.direction = direction
        self.is_valid = False
        self.pos_check()

    def do_move(self):
        if not self.is_valid:
            return

        l_row, l_col = self.pos
        if self.direction == 0:
            l_row -= 1
        elif self.direction == 1:
            l_col += 1
        elif self.direction == 2:
            l_row += 1
        elif self.direction == 3:
            l_col -= 1

        self.pos = (l_row, l_col)
        self.pos_check()

    def add_to_visited(self):
        if not self.is_valid:
            return
        if self.pos in Light.visited_set:
            return

        Light.visited_set.add(self.pos)

    def interact_tile(self, mirror_map):
        if not self.is_valid:
            return None

        l_row, l_col = self.pos
        l_tile = mirror_map[l_row][l_col]

        # Nothing happens with "."
        if l_tile == "/":
            if self.direction == 0:
                self.direction = 1
            elif self.direction == 1:
                self.direction = 0
            elif self.direction == 2:
                self.direction = 3
            elif self.direction == 3:
                self.direction = 2
        elif l_tile == "\\":
            if self.direction == 0:
                self.direction = 3
            elif self.direction == 1:
                self.direction = 2
            elif self.direction == 2:
                self.direction = 1
            elif self.direction == 3:
                self.direction = 0
        elif l_tile == "|":
            # Up and Down pass through
            # Right and Left split
            # By default, original points Up, copy points Down
            if self.direction % 2 == 1:
                if self.pos in Light.splitter_set:
                    self.is_valid = False
                    return None

                Light.splitter_set.add(self.pos)
                self.direction = 0
                return Light(self.pos, 2)
        elif l_tile == "-":
            # Right and Left pass through
            # Up and Down split
            # By default, original points Right, copy points Left
            if self.direction % 2 == 0:
                if self.pos in Light.splitter_set:
                    self.is_valid = False
                    return None

                Light.splitter_set.add(self.pos)
                self.direction = 1
                return Light(self.pos, 3)

        return None

    def pos_check(self):
        if not (0 <= self.pos[0] <= Light.pos_limits[0]):
            self.is_valid = False
        elif not (0 <= self.pos[1] <= Light.pos_limits[1]):
            self.is_valid = False
        else:
            self.is_valid = True

    @staticmethod
    def set_pos_constraints(mirror_map):
        Light.pos_limits = (len(mirror_map) - 1, len(mirror_map[0]) - 1)

    @staticmethod
    def set_starting_position(s_pos):
        Light.visited_set.add(s_pos)


def prep_solve(mirror_map):
    Light.set_pos_constraints(mirror_map)
    Light.visited_set = set()
    Light.splitter_set = set()


def solve(mirror_map, starting_light):
    Light.set_starting_position(starting_light.pos)

    light_list = [starting_light]
    steps = 0

    while len(light_list) != 0:
        # Interact with tiles
        split_light_list = []
        for light in light_list:
            split_light = light.interact_tile(mirror_map)
            if split_light is not None:
                split_light_list.append(split_light)
        light_list.extend(split_light_list)
        # Move all lights
        for light in light_list:
            light.do_move()
        # Filter invalid
        light_list = [light for light in light_list if light.is_valid]
        # Add to visited
        for light in light_list:
            light.add_to_visited()
        # Steps
        steps += 1

    # print(f"Steps: {steps}")
    # print(f"Final light count: {len(light_list)}")
    # print(f"Visited count: {len(Light.visited_set)}")

    return len(Light.visited_set)


if __name__ == "__main__":
    m_map = get_input("day16.txt")
    # print(*mirror_map, sep="\n")

    prep_solve(m_map)
    s_light = Light((0, 0), 1)
    print(solve(m_map, s_light))
