number_of_days = int(input("How many day's temperature?"))
total = 0
temp = []
for i in range(number_of_days):
    next_day = int(input("Day " + str(i+1) + "'s high temperature:"))
    temp.append(next_day)
    total += temp[i]

avg = round(total / number_of_days, 2)
print("\nAverage = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day(s) above average")
