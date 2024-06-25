from collections import deque


def get_input():
    with open('Day3\input.txt') as f:
        input = list(map(str.strip, f.readlines()))
    return input


def solution_One(input):

    schematic = input
    part_number = deque()

    y, x = 0, 0
    y_start, y_end = 0, 0
    x_start, x_end = 0, 0
    sum = 0

    for y in range(0, len(schematic)):
        for x in range(0, len(schematic[y])):

            if(not schematic[y][x].isalnum() and schematic[y][x] != '.'):

                if(y == 0): y_start = y
                elif(y == len(schematic)): y_end = y
                else: y_start, y_end = y-1, y+2

                if(x == 0): x_start = x
                elif(x == len(schematic[y])): x_end = x
                else: x_start, x_end = x-1, x+2

                for yy in range(y_start, y_end):
                    for xx in range(x_start, x_end):

                        if(schematic[yy][xx].isdigit()):
                            schematic[yy] = list(schematic[yy])
                            i = xx

                            while(1):
                                if(i > 0):
                                    if(schematic[yy][i-1].isdigit()):
                                        i -= 1
                                    else:
                                        break
                                else:
                                    break

                            while(1):
                                if(i < len(schematic[yy])):
                                    if(schematic[yy][i].isdigit()):
                                        part_number.append(schematic[yy][i])
                                        schematic[yy][i] = 'x'
                                        i += 1
                                    else:
                                        break
                                else:
                                    break

                            schematic[yy] = ''.join(schematic[yy])
                            sum += int(''.join(part_number))
                            part_number.clear()

    return sum


def solution_Two(input):

    schematic = input
    part_number = deque()
    part_numbers = deque()

    i = 0
    y, x = 0, 0
    y_start, y_end = 0, 0
    x_start, x_end = 0, 0
    sum = 0

    for y in range(0, len(schematic)):
        for x in range(0, len(schematic[y])):

            if(schematic[y][x] == '*'):

                if(y == 0): y_start = y
                elif(y == len(schematic)): y_end = y
                else: y_start, y_end = y-1, y+2

                if(x == 0): x_start = x
                elif(x == len(schematic[y])): x_end = x
                else: x_start, x_end = x-1, x+2

                for yy in range(y_start, y_end):
                    for xx in range(x_start, x_end):
                        i = 0
                        if(schematic[yy][xx].isdigit()):
                            schematic[yy] = list(schematic[yy])
                            i = xx

                            while(1):
                                if(i > 0):
                                    if(schematic[yy][i-1].isdigit()):
                                        i -= 1
                                    else:
                                        break
                                else:
                                    break

                            while(1):
                                if(i < len(schematic[yy])):
                                    if(schematic[yy][i].isdigit()):
                                        part_number.append(schematic[yy][i])
                                        i += 1
                                    else:
                                        i -= 1
                                        break
                                else:
                                    break
                            
                            schematic[yy] = ''.join(schematic[yy])
                            part_numbers.append(int(''.join(part_number)))
                            part_number.clear()
                        if(i > xx):
                            break

                if(len(part_numbers) == 2):
                    sum += (part_numbers[0] * part_numbers[1])
                part_numbers.clear()

    return sum


def main():
    print(f'Day 3.')
    
    print(f'Part 1 solution.')
    print(f'Sum is {solution_One(get_input())}.')

    print(f'Part 2 solution.')
    print(f'Sum is {solution_Two(get_input())}.')


if __name__ == '__main__':
    main()