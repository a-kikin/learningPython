a = 584

first = a // 100
second = (a // 10) % 10
last = a % 10

number = second * 100 + first * 10 + last
print(number)

