# Input provided:
# text file: c1.txt

# Todo: find first and last instance of number and create a 2 digit number. Once done, add all such 2 digit numbers.

# Data example: pqr3stu8vwx

import re

def main():
    with open("c1.txt", "r") as file:
        data_to_process = file.read().splitlines()
        # print(data_to_process)

    array_of_numbers = []
    first_digit = 0
    second_digit = 0

    for i in data_to_process:
        numbers = re.findall(r'[^a-z]', i)
        concatenated_numbers = ''.join(numbers)
        array_of_numbers.append(concatenated_numbers)

    # print(array_of_numbers)

    for i in array_of_numbers:
        first_digit = i[0]
        second_digit = i[-1]
        array_of_numbers[array_of_numbers.index(i)] = F"{first_digit}{second_digit}"


    # print(array_of_numbers)
    print(F"The sum of all the numbers is: {sum(map(int, array_of_numbers))}")

main()