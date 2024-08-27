'''Solution to problem for day 3 of 2021 advent of code.'''


def get_data():
    '''Returns data from text file'''
    with open("data.txt", "r") as f:
        return [line.strip() for line in f.readlines()]
