import sys

sides = []

for i in range(3):
    sides.append(int(sys.argv[i + 1]))

a = sides[0]
b = sides[1]
c = sides[2]

s = sum(sides) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
print(area)

