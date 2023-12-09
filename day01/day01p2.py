from day01p1 import get_first_num

str_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def replace_first_str_digits(string:str):
    lowest_index = 1000
    lowest_str_digit = ""
    flag = False
    for str_digit in str_digits.keys():
        if str_digit in string:
            current_index = string.find(str_digit)
            if current_index < lowest_index:
                lowest_index = current_index
                lowest_str_digit = str_digit
            flag = True

    if flag:
        l_index = lowest_index
        r_index = lowest_index + len(lowest_str_digit)
        new_string = string[:l_index] + \
            str(str_digits[lowest_str_digit]) + \
            string[l_index:]
        return new_string
    else:
        return string

def replace_last_str_digits(string:str):
    highest_index = -1
    highest_str_digit = ""
    flag = False
    for str_digit in str_digits.keys():
        if str_digit in string:
            current_index = string.rfind(str_digit)
            if current_index > highest_index:
                highest_index = current_index
                highest_str_digit = str_digit
            flag = True

    if flag:
        l_index = highest_index
        r_index = highest_index + len(highest_str_digit)
        new_string = string[:l_index] + \
            str(str_digits[highest_str_digit]) + \
            string[l_index:]
        return new_string
    else:
        return string


raw = []
values = []

with (open("day01.txt", "r") as file):
    for line in file:
        raw.append(line.strip())

raw = map(replace_first_str_digits, raw)
raw = map(replace_last_str_digits, raw)
raw = list(raw)

print(raw[0])

for line in raw:
    first = get_first_num(line)
    last = get_first_num(line[::-1])
    num = first * 10 + last
    values.append(num)

result = sum(values)
print(result)
