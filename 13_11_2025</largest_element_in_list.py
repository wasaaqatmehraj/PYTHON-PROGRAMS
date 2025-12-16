# List of numbers
numbers = [12, 45, 7, 89, 23]

# Assume first element is the largest
largest = numbers[0]

# Loop through the list
for num in numbers:
    if num > largest:
        largest = num

# Print the result
print("Largest number in the list is:", largest)
