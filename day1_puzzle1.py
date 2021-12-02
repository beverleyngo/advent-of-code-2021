measurements = []
f=open('day1_input.txt',"r")
for line in f:
    measurements.append(int(line.strip('\n')))

counter = 0
for i in range(len(measurements) - 1):
    if measurements[i + 1] > measurements[i]:
        counter += 1 

print(counter)