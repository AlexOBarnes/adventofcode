'''Solution to problem for day 3 of 2021 advent of code.'''

def get_data():
    '''Returns data from text file'''
    with open("data.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def get_epsilon(binary):
    '''Gets the inverse of gamma'''
    data = []
    for num in binary:
        if num == "1":
            data.append("0")
        else:
            data.append("1")
    return data

def process_data(data):
    '''Works out gamma'''
    length = len(data)
    gamma = []
    for i in range(len(data[0])):
        total = 0
        for binary in data:
            total += int(binary[i])
        if total/length > 0.5:
            gamma.append("1")
        else:
            gamma.append("0")

    epsilon = get_epsilon(gamma)
    return int("".join(gamma), 2)*int("".join(epsilon), 2), gamma, epsilon

def get_oxygen(seq_1, data):
    '''Finds oxygen value'''
    for i,bit in enumerate(seq_1):
        for index,num in enumerate(data):
            if bit == num[i]:
                data.pop(index)
            if len(data) == 1:
                return num
    return data[0]

def get_carbon(seq_2,data):
    '''Finds carbon value'''
    for i, bit in enumerate(seq_2):
        for index, num in enumerate(data):
            if bit == num[i]:
                data.pop(index)
            if len(data) == 1:
                return num

if __name__=="__main__":
    data = get_data()
    answer,most_common,least_common = process_data(data)
    print(answer)
    oxygen = get_oxygen(most_common,data)
    carbon = get_carbon(least_common,data)
    print(int(oxygen,2)*int(carbon,2))
