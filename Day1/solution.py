import os
import sys


def get_input():
    with open('Day1/input.txt') as f:
        input = list(map(str.strip, f.readlines()))
    return input


def solution_One(input):
    sum = 0
    for row in input:
        x = ""
        x = ''.join(filter(str.isdigit, row))
        sum += int(x[0] + x[-1])
    return sum


def solution_Two(input):
    numbers = {"one": 1, "two": 2, "three": 3,
               "four": 4, "five": 5, "six": 6,
               "seven": 7, "eight": 8, "nine": 9}
    sum = 0

    for row in input:
        temp_row = list(row)        
        temp_row_2 = list(row)

        for i in numbers.keys():
            while(1):
                pos = ''.join(temp_row).find(i)
                if(pos == -1): break
                temp_row[pos] = str(numbers.get(i))
                temp_row_2[pos] = str(numbers.get(i))
            temp_row = list(row)

        row = ''.join(temp_row_2)
        row = ''.join(filter(str.isdigit, row))
        sum += int(row[0] + row[-1])
    
    return sum


def main():
    print(f'Day 1.')

    print(f'Part 1 solution.')
    print(f'Sum is {solution_One(get_input())}.')

    print(f'Part 2 solution.')
    print(f'Sum is {solution_Two(get_input())}.')


if __name__ == '__main__':
    main()