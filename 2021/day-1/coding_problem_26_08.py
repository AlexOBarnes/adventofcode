'''Solution to advent of code 2021 day 1'''

def get_data():
    '''Returns data from text file'''
    with open("length.txt","r") as f:
        return [int(line.strip()) for line in f.readlines()]

def process_data(nums):
    '''Calculates how many are larger'''
    larger= 0
    for num1,num2 in zip(nums,nums[1:]):
        if num1<num2:
            larger+=1
    return larger

def process_triplets(nums):
    '''Calculates how many triplets are larger in sequence'''
    larger = 0
    for num1,num4 in zip(nums,nums[3:]):
        if (num1) < (num4):
            larger += 1

    return larger

if __name__ == "__main__":
    data = get_data()
    # print(data)
    answer = process_data(data)
    print(answer)
    answer_3 = process_triplets(data)
    print(answer_3)