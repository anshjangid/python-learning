
holidays = int(input("Enter number of holidays: "))

workday_play = 63
holiday_play = 127
norm = 30000
days_in_year = 365

workdays = days_in_year - holidays

total_play = 0

# Add playtime for holidays
for i in range(holidays):
    total_play += holiday_play

# Add playtime for workdays
for j in range(workdays):
    total_play += workday_play

if total_play > norm:
    print("Tom will run away")
    print(total_play - norm, "minutes more than norm")
else:
    print("Tom sleeps well")
    print(norm - total_play, "minutes less than norm")
