

def get_data():
    with open("length.txt","r") as f:
        return [int(line.strip()) for line in f.readlines()]

def process_data(nums):
    larger= 0
    for num1,num2 in zip(nums,nums[1:]):
        if num1<num2:
            larger+=1
    return larger

def process_triplets(nums):
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