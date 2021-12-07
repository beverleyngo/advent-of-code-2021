# Add each binary number from the puzzle input to a list
position1 = []
position2 = []
position3 = []
position4 = []
position5 = []
position6 = []
position7 = []
position8 = []
position9 = []
position10 = []
position11 = []
position12 = []

f=open('day3_input.txt',"r")
for line in f:
    position1.append(line[0])
    position2.append(line[1])
    position3.append(line[2])
    position4.append(line[3])
    position5.append(line[4])
    position6.append(line[5])
    position7.append(line[6])
    position8.append(line[7])
    position9.append(line[8])
    position10.append(line[9])
    position11.append(line[10])
    position12.append(line[11])

# Initialise the gamma and epsilon rate variables
gamma_rate = ''
epsilon_rate = ''

# Append the gamma and epsilon rate depending on rules
if max(position1, key=position1.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position2, key=position2.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position3, key=position3.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position4, key=position4.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position5, key=position5.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position6, key=position6.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position7, key=position7.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position8, key=position8.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position9, key=position9.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position10, key=position10.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position11, key=position11.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

if max(position12, key=position12.count) == '0':
    gamma_rate += '0'
    epsilon_rate += '1'
else:
    gamma_rate += '1'
    epsilon_rate += '0'

# Convert gamma and epsilon rates to decimal and multiply
print(str(int(gamma_rate,2) * int(epsilon_rate,2)))