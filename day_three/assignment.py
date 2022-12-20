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
def similar_characters(list1, list2):
    character_list = []
    for i in range(len(list1)):
        set1 = set(list1[i])
        set2 = set(list2[i])
        common_characters = set1.intersection(set2)
        same_characters = list(common_characters)
        character_list += same_characters
    return character_list
    
character_list = similar_characters(first_halve, second_halve)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priority_points = 0 

try:
    for i in character_list:
        priority_points += alphabet.index(i) + 1
except ValueError:
    print(f"Character {i} not found in alphabet")

print(priority_points)
