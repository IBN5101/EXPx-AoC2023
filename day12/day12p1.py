# Replaced functional springs "." into " " (space)
# To take advantage of the split function

def get_input(file_location):
    spring_map = []
    with (open(file_location, "r") as file):
        curr_row = file.readline().strip()
        while curr_row != "":
            springs, records = curr_row.split()
            springs = springs.replace(".", " ")
            records = list(map(int, records.split(",")))
            spring_map.append((springs, records))
            # print(springs, records)

            curr_row = file.readline().strip()
    return spring_map


def get_all_permutations(springs: str):
    permutation_stack = [springs]
    arrangement_list = []

    while permutation_stack:
        curr_springs = permutation_stack.pop()
        if "?" in curr_springs:
            for char in ("#", " "):
                new_spring = curr_springs.replace("?", char, 1)
                permutation_stack.append(new_spring)
        else:
            arrangement_list.append(curr_springs)

    return arrangement_list


def brute_force_one_spring(springs, records):
    arrangement_count = 0

    record_count = len(records)
    arrangement_list = get_all_permutations(springs)

    for arrangement in arrangement_list:
        spring_list = arrangement.split()
        if len(spring_list) != record_count:
            continue
        spring_list = list(map(len, spring_list))
        if spring_list == records:
            arrangement_count += 1

    return arrangement_count


def solve(spring_map):
    result = 0
    for springs, records in spring_map:
        result += brute_force_one_spring(springs, records)
    return result


if __name__ == "__main__":
    s_map = get_input("day12.txt")
    print(solve(s_map))
