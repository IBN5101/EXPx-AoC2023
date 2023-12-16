from day04p1 import get_input


def solve2(input_list):
    result = 0
    total_card_list = [1] * len(input_list)

    for i, line in enumerate(input_list):
        winning_num, check_num = line
        num_won = 0
        for num in check_num:
            if num in winning_num:
                num_won += 1

        if num_won > 0:
            for j in range(i + 1, i + num_won + 1):
                total_card_list[j] = total_card_list[j] + total_card_list[i]

        result += total_card_list[i]

    return result


if __name__ == "__main__":
    i_list = get_input("day04.txt")
    # print(*i_list, sep="\n")
    print(solve2(i_list))
