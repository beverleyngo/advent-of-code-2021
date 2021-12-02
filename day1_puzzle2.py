# Add each measurement from the puzzle input to a list
measurements = []
f=open('day1_input.txt',"r")
for line in f:
    measurements.append(int(line.strip('\n')))

# Iterate over each three-measurement sliding window and +1 to counter if it is an increase from previous
counter = 0
for i in range(len(measurements) - 3):
    if measurements[i + 1] + measurements[i + 2] + measurements[i + 3] > measurements[i] + measurements[i + 1] + measurements[i + 2]:
        counter += 1 

print(counter)