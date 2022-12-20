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

first_halve = []
second_halve = []

print(stripped[0])
for i in range(len(stripped)):
    first_halve.append(stripped[i][:midsection[i]])
    second_halve.append(stripped[i][midsection[i]:])

print(stripped[0])
print(first_halve[0] + second_halve[0])
print(first_halve[0])
print(second_halve[0])
