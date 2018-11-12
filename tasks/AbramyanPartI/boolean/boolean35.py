x1 = 3
y1 = 2
x2 = 5
y2 = 7

first = ((x1 % 2 == 0 and y1 % 2 > 0) or (x1 % 2 > 0 and y1 %2 == 0))
second = ((x2 % 2 == 0 and y2 % 2 > 0) or (x2 % 2 > 0 and y2 %2 == 0))

print(first, second)

print(first == second)
