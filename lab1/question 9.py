seconds = int(input("Enter seconds (1-86400): "))

if seconds >= 1 and seconds <= 86400:
    hours = seconds // 3600
    remaining = seconds % 3600
    minutes = remaining // 60
    secs = remaining % 60

    print(f"{hours:02}:{minutes:02}:{secs:02}")
else:
    print("Invalid input")