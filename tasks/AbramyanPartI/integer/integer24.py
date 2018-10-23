dayNumber = 235
dayStart = 1

week = dayNumber // 7
restDays = dayNumber % 7
rest = (dayNumber % 7) + dayStart

print(week, restDays, rest)
