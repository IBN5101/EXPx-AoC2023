def get_input(file_location):
    i_list = []
    with (open(file_location, "r") as file):
        curr_line = file.readline()
        while curr_line != "":
            curr_line = curr_line.strip().split()
            curr_line = list(map(int, curr_line))
            i_list.append(curr_line)

            curr_line = file.readline()
    return i_list


def recursive_prediction(value_list):
    # Guard
    if len(value_list) <= 1:
        raise Exception("Prediction failed.")

    # Base case: all values are 0
    test_0s = [i for i in value_list if i != 0]
    if len(test_0s) == 0:
        return 0

    # Recursive case:
    difference_list = []
    for i in range(len(value_list) - 1):
        difference_list.append(value_list[i + 1] - value_list[i])
    return value_list[-1] + recursive_prediction(difference_list)


if __name__ == "__main__":
    input_list = get_input("day09.txt")
    result_list = [recursive_prediction(value_list) for value_list in input_list]
    print(sum(result_list))
