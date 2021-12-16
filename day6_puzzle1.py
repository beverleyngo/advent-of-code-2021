# Read fish in to a list
f=open('day6_input.txt',"r")
for row in f:
    lanternfish = [int(fish) for fish in row.split(',')]

# Use recursion to calculate fish growth
def grow_fish(day, school_of_fish):
    # Stop recursion on day 80
    if day == 80:
        print(len(school_of_fish))
    else:
        count = 0
        updated_school = []
        for fish in school_of_fish:
            # Reduce fish timer if it is not zero
            if fish > 0:
                updated_school.append(fish - 1)
            # Reset fish time if it is zero and keep count of fish babies
            elif fish == 0:
                updated_school.append(6)
                count += 1 # Fish baby +1
        # Add fish babies to updated school of fish
        if count >= 1:
            updated_school += [8] * count
        # Recursion
        grow_fish(day+1, updated_school)

grow_fish(0,lanternfish)