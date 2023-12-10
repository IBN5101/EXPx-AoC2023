from day06p1 import get_input, simulate_race

races = []


def update_input():
    new_time = ""
    new_distance = ""
    for time, distance in races:
        new_time += str(time)
        new_distance += str(distance)
    new_time = int(new_time)
    new_distance = int(new_distance)

    # Singular super race
    return new_time, new_distance


def test_solution(time, distance, solution):
    for i in range(solution - 1, solution + 2):
        print(i, end=" ")
        print((time - i) * i > distance)


if __name__ == "__main__":
    races = get_input()
    new_time, new_distance = update_input()

    # JUST USE WOLFRAM ALPHA LMAO
    # Solve for:
    # -x^2 + time * x - distance = 0
    # Test the solutions to find final answer
    # solution = 42934734
    # test_solution(new_time, new_distance, solution)

    # Final solution
    lower = 5942248
    upper = 42934733
    print(upper - lower + 1)

    # Why not? Why not brute force it?
    print(simulate_race(new_time, new_distance))
