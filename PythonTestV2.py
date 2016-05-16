import os
import sys
import shutil


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
        three_items_inputted(first_input, second_input, third_input)


def one_item_inputted(first_input):
    true_or_false = check_valid_path(first_input)
    if true_or_false == True:
        print(os.path.abspath(first_input))
    else:
        sys.exit()


def two_items_inputted(first_input, second_input):
    if second_input == '-create':
        check_or_create(first_input, second_input)
    elif second_input.endswith('.txt'):
        print("lets go")
        fake =5
    else:
        print ("The second input is invalid, please try again")


def check_or_create(first_input, second_input):
    fake = 5
    print("good")




def three_items_inputted():
    fake = 5


def check_valid_path(filelocation):
    if os.path.exists(filelocation) == True:
        return True
    else:
        print('The file path is not valid, please retry with valid path....')
        return False


if __name__ == "__main__":
    main()