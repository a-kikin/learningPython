a = 1231

firstPare = a // 100
secondPare = a % 100

print(firstPare, secondPare)


firstOfSecondPare = secondPare // 10
secondOfSecondPare = secondPare % 10
switchedSecondPare = secondOfSecondPare * 10 + firstOfSecondPare

print(firstOfSecondPare, secondOfSecondPare, switchedSecondPare)
print(firstPare == switchedSecondPare)