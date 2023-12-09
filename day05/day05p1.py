# seed format:
# [seed, soil, fertilizer, water, light, temperature, humidity, location]
# almanac format:
# 0: seed -> soil
# 1: soil -> fertilizer
# 2: fertilizer -> water
# 3: water -> light
# 4: light -> temperature
# 5: temperature -> humidity
# 6: humidity -> location

def initialize():
    with (open("day05.txt", "r") as file):
        # Initialize
        sl = []
        al = []
        # Seed line
        first_line = file.readline()
        sl = first_line.strip().split(" ")
        sl.pop(0)
        sl = [int(value) for value in sl]

        # Everything else
        file.readline()  # Blank line
        almanac_entry = dict()
        current = file.readline()
        while current != "":
            # Header
            if ":" in current:
                almanac_entry = dict()
            # Separator
            elif current == "\n":
                al.append(almanac_entry)
            # Values
            else:
                # destination-source-range
                values = current.strip().split(" ")
                values = [int(value) for value in values]

                condition = (values[1], (values[1] + values[2] - 1))
                destination = values[0]
                almanac_entry[condition] = destination

            current = file.readline()
        # Last almanac entry
        al.append(almanac_entry)

        return sl, al


def seed_to_location(s, al):
    # Initialize seed
    current_seed = [0] * (7 + 1)
    current_seed[0] = s

    # See almanac format above
    for i in range(7):
        almanac_entry = al[i]
        current_source = current_seed[i]
        current_destination = current_source
        for conditional in almanac_entry:
            (source_min, source_max) = conditional
            if source_min <= current_source <= source_max:
                current_destination = almanac_entry[conditional] + (current_source - source_min)
                break
        current_seed[i + 1] = current_destination

    return current_seed[7]


if __name__ == "__main__":
    seed_list, almanac = initialize()

    lowest_location = 10000000000
    for seed in seed_list:
        current_location = seed_to_location(seed, almanac)
        if current_location < lowest_location:
            lowest_location = current_location
    print(lowest_location)