# Read the iput.txt file 

with open('day_one/input.txt', encoding='utf-8') as f: 
    content = f.readlines()

    total_calories = 0
    calorie_sums = []

    for i, v in enumerate(content):
        if i + 1 == len(content):
            total_calories += int(v)
            calorie_sums.append(total_calories)
        elif v not in ['\n']:
            total_calories += int(v)
        else:
            calorie_sums.append(total_calories)
            total_calories = 0 

print(calorie_sums)
print(max(calorie_sums))

sorted_list = sorted(calorie_sums,reverse=True)
print(sum(sorted_list[:3]))

