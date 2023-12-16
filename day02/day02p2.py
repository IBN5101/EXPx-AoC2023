from day02p1 import get_input


def solve2(game_list: list):
    game_powers = []

    for game in game_list:
        max_colors = [0, 0, 0]
        for turn in game:
            for color_ball in turn:
                ball_num, ball_color = color_ball
                if ball_num > max_colors[ball_color]:
                    max_colors[ball_color] = ball_num

        curr_game_power = max_colors[0] * max_colors[1] * max_colors[2]
        game_powers.append(curr_game_power)

    return sum(game_powers)


if __name__ == "__main__":
    g_list = get_input("day02.txt")
    print(solve2(g_list))
