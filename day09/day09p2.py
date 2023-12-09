from day09p1 import get_input


def recursive_prediction2(value_list):
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
    return value_list[0] - recursive_prediction2(difference_list)


if __name__ == "__main__":
    input_list = get_input("day09.txt")
    result_list = list(map(recursive_prediction2, input_list))
    print(sum(result_list))
