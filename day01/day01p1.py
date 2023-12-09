def get_first_num(string:str):
    for char in string:
        if char.isdigit():
            return int(char)


if __name__ == "__main__":
    values = []
    with (open("day01.txt", "r") as file):
        for line in file:
            first = get_first_num(line)
            last = get_first_num(line[::-1])
            num = first * 10 + last
            values.append(num)

    result = sum(values)
    print(result)
