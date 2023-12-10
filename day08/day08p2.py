from day08p1 import get_input

instruction_set = []
node_map = dict()
start_nodes = []
end_nodes = []


def update_input():
    for key in node_map.keys():
        if key[-1] == "A":
            start_nodes.append(key)
        elif key[-1] == "Z":
            end_nodes.append(key)


def solve2():
    # BRO BRUTE FORCE WILL NOT WORK
    # 20 billion is still too low
    # bruh
    current_nodes = start_nodes.copy()
    steps = 0
    flag_complete = False

    while not flag_complete:
        for i in range(len(current_nodes)):
            next_nodes_list = node_map[current_nodes[i]]
            current_instruction = instruction_set[steps % len(instruction_set)]
            current_nodes[i] = next_nodes_list[current_instruction]
        # print(current_nodes)
        steps += 1

        # Debug
        # if steps % 10000000 == 0:
        #     print(steps)

        for node in current_nodes:
            flag_complete = True
            if node not in end_nodes:
                flag_complete = False
                break

    return steps


def solve3():
    current_nodes = start_nodes.copy()
    steps = 0

    test_node = current_nodes[5]
    # 0: 11567
    # 1: 19637
    # 2: 15871
    # 3: 21251
    # 4: 12643
    # 5: 19099
    last_found = 0
    for i in range(100000):
        if test_node in end_nodes:
            print(test_node, steps % len(instruction_set),
                  steps, steps - last_found)
            last_found = steps

        next_nodes_list = node_map[test_node]
        current_instruction = instruction_set[steps % len(instruction_set)]
        test_node = next_nodes_list[current_instruction]

        steps += 1
        if steps % 10000000 == 0:
            print(steps)


if __name__ == "__main__":
    instruction_set, node_map = get_input("day08.txt")
    update_input()
    # solve3()
    # Use solve3() to get the multiple of each starting node
    # This number is when the node reaches an ending node
    # Surprisingly this loops exactly (yay) (it was designed that way)
    # Use Wolfram Alpha to get the LCM of the 6 values
    print(11567 * 19637 * 15871 * 21251 * 12643 * 19099)
    print(13133452426987)  # Thanks, Wolfram Alpha

    # Final notes: Checking the subreddit,
    # this problem was specifically designed to be used with LCM
