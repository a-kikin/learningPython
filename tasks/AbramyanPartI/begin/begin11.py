import math

oneInt = int(input('Input your first random int: '))
secondInt = int(input('Input your second random int: '))

sumSquare = math.fabs(oneInt)**2 + math.fabs(secondInt)**2
minSquare = math.fabs(oneInt)**2 - math.fabs(secondInt)**2
bSquare = math.fabs(oneInt)**2 * math.fabs(secondInt)**2
cSquare = math.fabs(oneInt)**2 / math.fabs(secondInt)**2

print('Your sumsquare is: ', sumSquare, '\n', 'minsquare: ', minSquare, '\n',
      'bsquare: ', bSquare, '\n', 'csq: ', cSquare)
