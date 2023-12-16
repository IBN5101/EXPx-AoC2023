def turn_string_to_tuple(turn_string):
    color_dict = {
        "red": 0,
        "green": 1,
        "blue": 2
    }

    num_and_color = turn_string.split()
    turn_num = int(num_and_color[0])
    turn_color = color_dict[num_and_color[1]]

    return turn_num, turn_color


def get_input(file_location):
    game_list = []
    with (open(file_location, "r") as file):
        curr_line = file.readline()
        while curr_line != "":
            curr_line = curr_line.strip().split(":")
            curr_line = curr_line[1].strip().split(";")

            curr_game = []
            for sentence in curr_line:
                turn = sentence.split(",")
                turn = [turn_string_to_tuple(i.strip()) for i in turn]
                curr_game.append(turn)
            game_list.append(curr_game)

            curr_line = file.readline()
    return game_list


def solve(game_list: list, ball_bag: list):
    result = 0

    for i, game in enumerate(game_list):
        game_possible = True
        for turn in game:
            for color_ball in turn:
                ball_num, ball_color = color_ball
                if ball_num > ball_bag[ball_color]:
                    game_possible = False
                    break
            if not game_possible:
                break

        if game_possible:
            result += i + 1

    return result


if __name__ == "__main__":
    g_list = get_input("day02.txt")
    b_bag = [12, 13, 14]  # Red, Green, Blue
    # print(*g_list, sep="\n")
    print(solve(g_list, b_bag))
