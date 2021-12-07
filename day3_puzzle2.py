numbers = []
f=open('day3_input.txt',"r")
for line in f:
    numbers.append(line.strip('\n'))

def find_oxygen(numbers, x):
    if len(numbers) == 1:
        # print(numbers)
        print(str(int(numbers[0],2)))
        # return int(numbers[0],2)
    else:
        list_0 = []
        list_1 = []
        for number in numbers:
            if number[x] == '0':
                list_0.append(number)
            else:
                list_1.append(number)
        if len(list_0) > len(list_1):
            find_oxygen(list_0, x+1)
        elif len(list_1) > len(list_0) or len(list_1) == len(list_0):
            find_oxygen(list_1, x+1)

def find_co2(numbers, x):
    if len(numbers) == 1:
        # print(numbers)
        print(str(int(numbers[0],2)))
        # return int(numbers[0],2)
    else:
        list_0 = []
        list_1 = []
        for number in numbers:
            if number[x] == '0':
                list_0.append(number)
            else:
                list_1.append(number)
        if len(list_0) < len(list_1) or len(list_1) == len(list_0):
            find_co2(list_0, x+1)
        elif len(list_1) < len(list_0):
            find_co2(list_1, x+1)
find_oxygen(numbers, 0)
find_co2(numbers, 0)
# print(str(find_oxygen(numbers, 0)))
# print(str(find_oxygen(numbers, 0) * find_co2(numbers, 0)))
# print(str(int(find_oxygen(numbers, 0)) * int(find_co2(numbers, 0))))