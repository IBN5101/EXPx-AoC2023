# Global var
races = []


def get_input():
    # Read
    file_location = "day06.txt"
    with (open(file_location, "r") as file):
        # Time list
        times = file.readline().strip().split()
        times.pop(0)
        times = [int(i) for i in times]
        # Distance list
        distances = file.readline().strip().split()
        distances.pop(0)
        distances = [int(i) for i in distances]
        # Combined
        for i in range(len(times)):
            races.append((times[i], distances[i]))
    return races


def simulate_race(time, distance):
    # Returns the margin of error of each race
    # lower and upper are time holding the button
    lower = 1
    upper = time - 1
    # Lower bound
    for i in range(lower, upper, 1):
        speed = i
        remaining_time = time - i
        if speed * remaining_time > distance:
            break
        lower += 1
    # Upper bound
    for i in range(upper, lower, -1):
        speed = i
        remaining_time = time - i
        if speed * remaining_time > distance:
            break
        upper -= 1
    # Margin
    return abs(upper - lower) + 1


if __name__ == "__main__":
    races = get_input()
    margins = []
    for time, distance in races:
        margins.append(simulate_race(time, distance))

    final_result = 1
    for i in margins:
        final_result *= i
    print(final_result)
