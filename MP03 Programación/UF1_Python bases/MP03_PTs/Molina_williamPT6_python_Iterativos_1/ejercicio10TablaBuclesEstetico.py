x = 0

for x in range (10):
    if x <= 10:
        x += 1
        print(str(x).ljust(2), end=' ')

print("")
x = 2

for x in range (2, 21, 2):
    print(str(x).ljust(2), end=' ')

print("")
x = 20

for x in range (20, 39, 2):
    print(str(x).ljust(2), end=' ')

print("")
x = 10

for x in range (10, 31, 4):
    print(str(x).ljust(2), end=' ')

print("")
x = 40

for x in range (40, -1, -5):
    print(str(x).ljust(2), end=' ')
