# Input provided:
# text file: c1.txt

# Todo: find first and last instance of number and create a 2 digit number. Once done, add all such 2 digit numbers.

# Data example: pqr3stu8vwx

import re

def main():
    # Open the file for reading.
    with open("c1.txt", "r") as file:
        # Read a single line from the file.
        data_to_process = file.read().splitlines()

    array_of_numbers = []
    first_digit = 0
    second_digit = 0

    for i in data_to_process:
        numbers = re.findall(r'\d+', i)
        array_of_numbers.extend(map(str, numbers))




    print(array_of_numbers)
    print(F"The sum of all the numbers is: {sum(map(int, number_array))}")

main()