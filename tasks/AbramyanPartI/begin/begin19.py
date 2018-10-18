import math

x1 = 4
y1 = 10
x2 = 40
y2 = 25

bigSize = math.fabs(x1 - x2)
smallSize = math.fabs(y1 - y2)
p = bigSize * 2 + smallSize * 2
s = bigSize * smallSize

print(bigSize, smallSize, p, s)