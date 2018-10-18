import math

a = int(input('Input a of your toungle: '))
b = int(input('Input b of your toungle: '))

c = round(math.sqrt(a**2 + b**2), 2)
p = a + b + c

print('Your c is: ', c, '\n', 'Your p is: ', p)
