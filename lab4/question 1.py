
#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and years of service and print the net bonus amount. 

salary = float(input("Enter your salary: "))
years = int(input("Enter your years of service: "))

if years > 5:
    bonus = 0.05 * salary
    print("Net bonus amount:", bonus)
else:
    print("No bonus")
