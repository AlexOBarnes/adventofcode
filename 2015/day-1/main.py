'''Solution to advent of code day 1 2015'''
from collections import Counter

def get_data() -> str:
    '''Gets the string from data.txt'''
    with open('data.txt','r') as f:
        data =  f.readlines()
    return data[0]

def count_floors(moves:str) -> int:
    '''Counts the number of parentheses and calculates the floor'''
    count = Counter(moves)

    return count['(']-count[')']

def first_basement(moves:str) -> int:
    counter = 0
    index = 0
    for parens in moves:
        index += 1
        if parens == '(':
            counter += 1
        if parens == ')':
            counter -= 1
        if counter < 0:
            return index

if __name__ == '__main__':
    move_data = get_data()
    print(count_floors(move_data))
    print(first_basement(move_data))