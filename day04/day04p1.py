def get_input(file_location):
    input_list = []
    with (open(file_location, "r") as file):
        curr_line = file.readline().strip()
        while curr_line != "":
            curr_line = curr_line.split(":")
            curr_line = curr_line[1].split("|")
            winning_num = curr_line[0].strip().split()
            winning_num = list(map(int, winning_num))
            check_num = curr_line[1].strip().split()
            check_num = list(map(int, check_num))

            input_list.append((winning_num, check_num))
            curr_line = file.readline().strip()

    return input_list


def solve(input_list):
    result = 0
    for line in input_list:
        winning_num, check_num = line
        num_won = 0
        for num in check_num:
            if num in winning_num:
                num_won += 1

        if num_won > 0:
            result += 2 ** (num_won - 1)

    return result


if __name__ == "__main__":
    i_list = get_input("day04.txt")
    # print(*i_list, sep="\n")
    print(solve(i_list))
