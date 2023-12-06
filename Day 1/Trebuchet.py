# Input provided:
# text file: c1.txt

# Todo: find first and last instance of number and create a 2 digit number. Once done, add all such 2 digit numbers.

# Data example: pqr3stu8vwx

import re

def main():
    with open("ex2.txt", "r") as file:
        data_to_process = file.read().splitlines()
        print(data_to_process)

    conversion_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five":5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }
    input_data = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]

    array_of_numbers = []
    first_digit = 0
    second_digit = 0

    for i in data_to_process:
        numbers = re.findall(r'[a-z]', i)
        # check if the number is in the conversion map
        concatenated_numbers = ''.join(numbers)
        array_of_numbers.append(concatenated_numbers)

    print(array_of_numbers)

    for i in array_of_numbers:
        # check conversion_map is a substring of i
        for key in conversion_map:
            if key in i:
                i = i.replace(key, str(conversion_map[key]))
        print(i)

    print(array_of_numbers)
    # print(F"The sum of all the numbers is: {sum(map(int, array_of_numbers))}")

main()