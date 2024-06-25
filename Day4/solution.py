from collections import deque

def get_input():
    with open('Day4\input.txt') as f:
        input = list(map(str.strip, f.readlines()))
    return input

def solution_One(input):
    sum = 0
    for card in input:
        points = 0
        _, card = card.split(':')
        winning_num, my_num = card.split('|')
        winning_num = set(map(str.strip, winning_num.split()))
        my_num = set(map(str.strip, my_num.split()))

        for num in my_num:
            if(num in winning_num):
                if(points == 0): points = 1
                else: points *= 2

        sum += points
    return sum
    

def main():
    print(f'Day 4.')
    
    print(f'Part 1 solution.')
    print(f'Sum is {solution_One(get_input())}.')


if __name__ == '__main__':
    main()