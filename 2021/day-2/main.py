'''Solution to 2021 advent of code day 2'''


def get_data():
    '''Returns data from text file'''
    with open("data.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def calculate_position(movements):
    "Calculates position using only horizontal and depth variables"
    horizontal = 0
    depth = 0
    for move in movements:
        if "forward" in move:
            horizontal += int(move.split(" ")[1])
        if "down" in move:
            depth += int(move.split(" ")[1])
        if "up" in move:
            depth -= int(move.split(" ")[1])
    return horizontal*depth


def calculate_position_2(movements):
    '''Calculates the position using aim'''
    horizontal = 0
    aim = 0
    depth = 0
    for move in movements:
        if "forward" in move:
            horizontal += int(move.split(" ")[1])
            if aim:
                depth += aim*int(move.split(" ")[1])
        if "down" in move:
            aim += int(move.split(" ")[1])
        if "up" in move:
            aim -= int(move.split(" ")[1])
    return horizontal*depth

if __name__ == "__main__":
    data = get_data()
    print(data)
    distance = calculate_position(data)
    print(distance)
    distance_2 = calculate_position_2(data)
    print(distance_2)