with open('day_three/inputs.txt','r') as f:
    content = f.readlines()

stripped = []

for i in content:
    stripped.append(i[:-1])

badges = []
group_sizes = 3


def find_badge_character_test(contents):
    group = 1
    for i, v in enumerate(contents):
        # print(f'{i} is the person')
        if (i+1) % 3 != 0:
            print(f'{i} is in group {group}')
        elif (i+1) % 3 == 0:
            print(f'{i} is in group {group}')
            group += 1
             
grouped_bags = []

def find_badge_character(content):
    complete_bag = ''
    for i, v in enumerate(content):
        if (i+1) % 3 != 0:
            complete_bag += (v + '-')
        elif (i+1) % 3 == 0:
            complete_bag += (v)
            grouped_bags.append(complete_bag)
            complete_bag = ''

def i_honestly_dont_even_know(items_list):
    common_characters_list = []
    for i in range(len(items_list)):
        item1, item2, item3 = items_list[i].split('-')
        set1, set2, set3 = set(item1), set(item2), set(item3)
        common_characters_list += list(set1.intersection(set2, set3))
    return common_characters_list

find_badge_character(stripped)

group_common_characters = i_honestly_dont_even_know(grouped_bags)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

priority_points = 0 

try:
    for i in group_common_characters:
        priority_points += alphabet.index(i) + 1
except ValueError:
    print(f"Character {i} not found in alphabet")

print(priority_points)

