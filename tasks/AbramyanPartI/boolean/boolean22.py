a = 122

first = a // 100
second = a // 10 % 10
third = a % 10

print(first, second, third)

print(first < second < third or first > second > third)