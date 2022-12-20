#open and read the input file 
with open('day_three/inputs.txt','r') as f:
    content = f.readlines()

# strip the last character of which is an \n characture 
stripped = []

for i in content:
    stripped.append(i[:-1])

#find the midsection of each input item 
midsection = []

for i in range(len(stripped)):
    midsection.append(int(len(stripped[i]) / 2))

# get a list with the first and second section of each input
first_halve = []
second_halve = []

for i in range(len(stripped)):
    first_halve.append(stripped[i][:midsection[i]])
    second_halve.append(stripped[i][midsection[i]:])

# compare the values in each input half
def similar_characters(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    common_characters = set1.intersection(set2)
    same_characters = list(common_characters)
    print(f'in string number {i} the similar character is {same_characters}')

for i in range(len(stripped)):
    similar_characters(first_halve[i], second_halve[i])

print(first_halve[-2] + '--' + second_halve[-2])