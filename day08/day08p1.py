instruction_set = []
node_map = dict()


def get_input(file_location):
    # Initialize
    i_set = []
    n_map = dict()

    with (open(file_location, "r") as file):
        first_line = file.readline().strip()
        first_line = first_line.replace("L", "0")
        first_line = first_line.replace("R", "1")
        i_set = list(first_line)
        i_set = [int(i) for i in i_set]

        file.readline()  # Blank

        current_line = file.readline()
        while current_line != "":
            current_node, next_nodes = current_line.strip().split(" = ")
            next_node_list = next_nodes[1:-1].split(", ")

            n_map[current_node] = next_node_list

            current_line = file.readline()

    return i_set, n_map


def solve():
    current_node = "AAA"
    end_node = "ZZZ"
    steps = 0

    while current_node != end_node:
        next_nodes_list = node_map[current_node]
        current_instruction = instruction_set[steps % len(instruction_set)]
        current_node = next_nodes_list[current_instruction]

        steps += 1

    return steps


if __name__ == "__main__":
    instruction_set, node_map = get_input("day08.txt")
    print(solve())
