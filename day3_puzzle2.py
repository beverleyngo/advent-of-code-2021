# Read numbers from input file
numbers = []
f=open('day3_input.txt',"r")
for line in f:
    numbers.append(line.strip('\n'))

# Use recursion to find the oxygen generator rating
def find_oxygen(numbers, x):
    # If there is one number remaining, return it
    if len(numbers) == 1:
        return int(numbers[0],2)
    else:
        list_0 = []
        list_1 = []
        # Add each number to list based on the bit value
        for number in numbers:
            if number[x] == '0':
                list_0.append(number)
            else:
                list_1.append(number)
        # Recursion
        if len(list_0) > len(list_1):
            return find_oxygen(list_0, x+1)
        elif len(list_1) > len(list_0) or len(list_1) == len(list_0):
            return find_oxygen(list_1, x+1)

# Use recursion to find the CO2 scrubber rating
def find_co2(numbers, x):
    # If there is one number remaining, return it
    if len(numbers) == 1:
        return int(numbers[0],2)
    else:
        list_0 = []
        list_1 = []
        # Add each number to list based on the bit value
        for number in numbers:
            if number[x] == '0':
                list_0.append(number)
            else:
                list_1.append(number)
        # Recursion
        if len(list_0) < len(list_1) or len(list_1) == len(list_0):
            return find_co2(list_0, x+1)
        elif len(list_1) < len(list_0):
            return find_co2(list_1, x+1)

# Convert binary to decimal and multiply
print(str(find_oxygen(numbers, 0) * find_co2(numbers, 0)))