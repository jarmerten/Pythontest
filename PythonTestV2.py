import os
import sys


def main():
    first_input = user_input1()
    second_input = user_input2()
    third_input = user_input3()
    total_input = number_of_inputs(first_input, second_input, third_input)
    run_correct_command(first_input, second_input, third_input, total_input)


def user_input1():
    first_input = sys.argv[1]
    return first_input

def user_input2():
    try:
        sys.argv[2]
    except IndexError:
        second_input = 'noinput'
    else:
        second_input = sys.argv[2]
    return second_input


def user_input3():
    try:
        sys.argv[3]
    except IndexError:
        third_input = 'noinput'
    else:
        third_input = sys.argv[3]
    return third_input


def number_of_inputs(first_input, second_input, third_input):
    paths_total = 0
    if second_input == 'noinput':
        paths_total = 1
    elif third_input == 'noinput':
        paths_total = 2
    else:
        paths_total = 3
    return paths_total


def run_correct_command(first_input, second_input, third_input, total_input):
    if total_input == 1:
        one_item_inputted(first_input)
    elif total_input == 2:
        two_items_inputted(first_input, second_input)
    else:
        if third_input == '-create':
            three_items_inputted(first_input, second_input)
        else:
            print("The third input is incorrect, please reenter everything correctly")


def one_item_inputted(first_input):
    true_or_false = check_valid_path(first_input)
    if true_or_false == True:
        print(os.path.abspath(first_input))
    else:
        print("File path does not exist")


def two_items_inputted(first_input, second_input):
    if second_input == '-create':
        check_or_create(first_input)
    elif second_input.endswith('.txt'):
        store_absolute_in_file_or_ignore(first_input, second_input)
    else:
        print("The second input is invalid, please try again")


def check_or_create(first_input):
    true_or_false = check_valid_path(first_input)
    if true_or_false == True:
        print("Cannot create new path, path already exists. Please try a different one")
    else:
        print("New folder created")
        os.makedirs(first_input)
        print(os.path.abspath(first_input))


def store_absolute_in_file_or_ignore(first_input, second_input):
    with open(first_input) as relative_paths:
        for each_line in relative_paths:
            true_or_false = check_valid_path(each_line)
            new_file = open(second_input, 'w')
            if true_or_false == True:
                new_file.write(os.path.abspath(each_line) + '\n')


def three_items_inputted(first_input, second_input):
    with open(first_input) as relative_paths:
        new_file = open(second_input, 'w')
        for each_line in relative_paths:
            true_or_false = check_valid_path(each_line)
            if true_or_false == True:
                new_file.write(os.path.abspath(each_line) + '\n')
            else:
                each_line = each_line[:-1]
                os.makedirs(os.path.abspath(each_line))
                new_location = (os.path.abspath(each_line) + '\n')
                new_file.write(new_location)

def check_valid_path(filelocation):
    if os.path.exists(filelocation) == True:
        return True
    else:
        return False


if __name__ == "__main__":
    main()