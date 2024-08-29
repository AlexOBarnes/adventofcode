'''Solution to Day 2 of the 2015 advent of code problems'''

def calculate_area(sides:list[int]) -> list[int]:
    '''Calculates the area of each side of the cuboid'''
    areas = []
    for i,num in enumerate(sides):
        if i == 0:
            areas.append(2*num*sides[i+1])
            areas.append(2*num*sides[i+2])
        if i == 1:
            areas.append(2*num*sides[i+1])
    return areas

def find_sides(dimensions:str)->list[int]:
    '''Returns a list of sides'''
    if isinstance(dimensions,str):
        dimension_list = dimensions.strip().split("x")
        return [int(num) for num in dimension_list]
    raise TypeError("Dimensions are not a string")

def get_data() -> list[str]:
    '''Reads data in from data.txt'''
    with open('data.txt','r', encoding='UTF-8') as f:
        data = f.readlines()
    return data

def get_wrapping(sides:list[int]) -> int:
    '''Returns the total wrapping needed'''
    return sum(sides)+(min(sides)/2)

def get_perimeter(sides: list[int]) -> int:
    '''Returns the perimeter of te shortest side'''
    side1 = sides.pop(sides.index(min(sides)))
    side2 = sides.pop(sides.index(min(sides)))
    return 2*(side1+side2)

def get_bow(sides: list[int]) -> int:
    '''Returns the cubic volume of the cuboid'''
    product = 1
    for num in sides:
        product *= num
    return product


if __name__ == '__main__':
    measurements = get_data()
    total_wrapping = 0
    total_ribbon = 0
    for present in measurements:
        sides = find_sides(present)
        area = calculate_area(sides)
        total_wrapping += get_wrapping(area)
        perimeter = get_perimeter(sides)
        bow = get_bow(sides)
        total_ribbon += perimeter+bow
    print(total_wrapping)
    print(total_ribbon)