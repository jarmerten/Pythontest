import unittest
from Pythontest import PythonTestV2
import os
import sys


class Testing(unittest.TestCase):

    def test_number_of_inputs(self):
        first = 'five'
        second  = 'noinput'
        third = 'noinput'
        total = PythonTestV2.number_of_inputs(first,second, third)
        self.assertEqual(total, 1)


    def test_number_of_inputs1(self):
        first = 'five'
        second  = 'six'
        third = 'noinput'
        total = PythonTestV2.number_of_inputs(first,second, third)
        self.assertEqual(total, 2)


    def test_number_of_inputs2(self):
        first = 'five'
        second  = 'six'
        third = 'seven'
        total = PythonTestV2.number_of_inputs(first,second, third)
        self.assertEqual(total, 3)


    def test_one_item_inputted2(self):
        first = 'WorkOrder.txt'
        PythonTestV2.one_item_inputted(first)
        self.assertLogs("C:\\Users\\Jared Merten\\PycharmProjects\\Week11Test\\Pythontest\\WorkOrder.txt")

    def test_one_item_inputted3(self):
        first = 'incorrect'
        PythonTestV2.one_item_inputted(first)
        self.assertLogs("File path does not exist")

    def test_two_items_inputted(self):
        first = 'king'
        second = 'mike'
        PythonTestV2.two_items_inputted(first,second)
        self.assertLogs("The second input is invalid, please try again")

    def test_check_or_create(self):
        first = 'WorkOrder.txt'
        PythonTestV2.check_or_create(first)
        self.assertLogs("Cannot create new path, path already exists. Please try a different one")

    def test_check_or_create1(self):
        first = 'Kings'
        PythonTestV2.check_or_create(first)
        self.assertLogs("New folder created")

    def test_check_valid_path(self):
        first = 'WorkOrder.txt'
        true_or_false = PythonTestV2.check_valid_path(first)
        self.assertEqual(true_or_false, True)

    def test_check_valid_path2(self):
        first = 'places.txt'
        true_or_false = PythonTestV2.check_valid_path(first)
        self.assertEqual(true_or_false, False)

    def test_input(self):
        noinput = PythonTestV2.user_input3()
        self.assertEqual(noinput, 'noinput')

    def test_input(self):
        noinput = PythonTestV2.user_input2()
        self.assertEqual(noinput, 'true')

    def test_store_absolute_in_file_or_ignore(self):
        first = 'WorkOrder.txt'
        second = 'testcreatesfile.txt'
        PythonTestV2.store_absolute_in_file_or_ignore(first,second)
        self.assertEqual(os.path.abspath(second), "C:\\Users\\Jared Merten\\PycharmProjects\\Week11Test\\Pythontest\\testcreatesfile.txt")

    def three_items_inputted(self):
        first = 'WorkOrder.txt'
        second = 'testcreatesanothernewfile.txt'
        PythonTestV2.store_absolute_in_file_or_ignore(first,second)
        self.assertEqual(os.path.abspath(second), "C:\\Users\\Jared Merten\\PycharmProjects\\Week11Test\\Pythontest\\testcreatesanothernewfile.txt")


    def test_run_correct_command(self):
        first_input = 'test'
        second_input = 'test'
        third_input = 'notcreate'
        total_input = 3
        PythonTestV2.run_correct_command(first_input,second_input,third_input, total_input)
        self.assertLogs("The third input is incorrect, please reenter everything correctly")

if __name__ == '__main__':
    unittest.main()
