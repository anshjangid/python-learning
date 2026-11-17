raw_input = input("Enter integers separated by spaces: ")
numbers = []
current_num = ""

for char in raw_input:
    if char == " ":
        if current_num != "":
            numbers += [int(current_num)]
            current_num = ""
    else:
        current_num += char
if current_num != "":
    numbers += [int(current_num)]

# i. Find Sum
total_sum = 0
for num in numbers:
    total_sum += num

# ii. Find Product
total_product = 1 if len(numbers) > 0 else 0
for num in numbers:
    total_product *= num

# iii. Find Smallest
smallest = numbers[0] if len(numbers) > 0 else None
for num in numbers:
    if num < smallest:
        smallest = num

print("Sum:", total_sum)
print("Product:", total_product)
print("Smallest:", smallest)