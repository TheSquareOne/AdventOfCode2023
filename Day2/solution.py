def get_input():
    with open('Day2/input.txt') as f:
        input = f.readlines()
    return input


def solution_One(input):
    bag = { 'red': 12,
            'green': 13,
            'blue': 14 }

    sum = 0
    possible = 0

    for game in input:
        id, cubes = game.split(':')

        for i in cubes.split(';'):
            for y in i.split(','):
                x = y.strip().split(' ')
                
                if(int(x[0]) > bag.get(x[1])):
                    possible = 0
                    break
                else:
                    possible = 1

            if(possible == 0):
                break

        if(possible == 1):
            sum += int(id.split()[1])

    return sum


def solution_Two(input):
    sum = 0
    
    for game in input:
        cubes_max = {'red': 0,
                    'green': 0,
                    'blue': 0}

        id, cubes = game.split(':')
        for i in cubes.split(';'):
            for y in i.split(','):
                x = y.strip().split(' ')

                if(int(cubes_max.get(x[1])) < int(x[0])):
                    cubes_max.update({str(x[1]):x[0]})

        mul = 1
        for x in cubes_max.values():
            mul *= int(x)
        sum += mul

    return sum


def main():
    print(f'Day 2.')
    
    print(f'Part 1 solution.')
    print(f'Sum is {solution_One(get_input())}.')

    print(f'Part 2 solution.')
    print(f'Sum is {solution_Two(get_input())}.')


if __name__ == '__main__':
    main()