
hours = int(input("Enter hours (0-23): "))
minutes = int(input("Enter minutes (0-59): "))

for i in range(15):
    minutes = 15+minutes
    if minutes == 60:
        minutes=0
        hours = 1+hours
    if hours == 24:
        hours=0
print(hours,":",minutes)





