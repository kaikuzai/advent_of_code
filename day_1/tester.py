lister = [2, 2, 2, 'stop', 3, 3, 3]

lijstje = []
counter = 0

for i, v in enumerate(lister):

    if i + 1 == len(lister):
        counter += v
        lijstje.append(counter) 
        print(i, v, counter)
    elif v not in ['stop']:
        counter += v
        print(i, v, counter)
    else:
        lijstje.append(counter)
        counter = 0
        print(i, v, counter)

print(lijstje)
print(max(lijstje))