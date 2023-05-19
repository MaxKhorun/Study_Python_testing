
L = []
with open(f'D:\SF\Labirinth.txt') as file:
    for line in file:
        L.append(line.replace('\n', '').split(' '))

print(L)
