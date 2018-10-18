x1 = 23
y1 = 2
x2 = 15
y2 = 6
x3 = 64
y3 = 15

firstSide = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
secondSide = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
thirdSide = ((x3 - x1)**2 + (y3 - y1)**2)**0.5

p = firstSide + secondSide + thirdSide
s = (p * (p - firstSide)*(p - secondSide)*(p - thirdSide))**0.5

print(firstSide, secondSide, thirdSide, p, s)
