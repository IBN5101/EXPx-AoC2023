from day05p1 import initialize, seed_to_location


def lowest_location_search(al, s_list):
    lowest_location = 10000000000
    for seed in s_list:
        current_location = seed_to_location(seed, al)
        if current_location < lowest_location:
            lowest_location = current_location
    return lowest_location


def initialize2():
    with (open("day05.txt", "r") as file):
        # Seed line
        first_line = file.readline()
        sl = first_line.strip().split(" ")
        sl.pop(0)
        sl = [int(value) for value in sl]

        sl_start = sl[0::2]
        sl_range = sl[1::2]
        # Note: There are 10 value pairs
        sl = [(sl_start[i], sl_start[i] + sl_range[i]) for i in range(10)]
        return sl


def search_algorithm(search_start, search_end, al):
    # Initialize
    s_min = search_start
    s_max = search_end
    gap = s_max - s_min
    # Divide by 10
    while gap >= 10000:
        candidates = []
        small_gap = gap // 10
        for i in range(10):
            candidate = s_min + small_gap * i
            candidates.append(candidate)
        candidates.append(s_max)

        lowest_location = 10000000000
        lowest_candidate = 0
        for candidate in candidates:
            current_location = seed_to_location(candidate, al)
            if current_location < lowest_location:
                lowest_location = current_location
                lowest_candidate = candidate

        if lowest_candidate == s_min:
            s_max = s_min + small_gap * 2
        elif lowest_candidate == s_max:
            s_min = s_max - small_gap * 2
        else:
            s_min = lowest_candidate - small_gap
            s_max = lowest_candidate + small_gap

        gap = s_max - s_min

    # Less than 10000 seed candidates remaining:
    return lowest_location_search(al, range(s_min, s_max))


if __name__ == "__main__":
    _, almanac = initialize()
    seed_list = initialize2()
    # print(seed_list)

    results = []
    for (min_bound, max_bound) in seed_list:
        results.append(search_algorithm(min_bound, max_bound, almanac))
    print(min(results))
