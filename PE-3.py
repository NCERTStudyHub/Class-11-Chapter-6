# Write a program that prints minimum and maximum of five numbers entered by the user.
# Programming Exercises - 3

def find_min_max(numbers):
    """Finds and returns the minimum and maximum values from a list of numbers."""
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

# Get user input
numbers = []

print("Enter five numbers:")
for i in range(5):
    while True:
        try:
            num = float(input(f"Number {i + 1}: "))  # Accepting float for more flexibility
            numbers.append(num)
            break  # Exit loop if input is valid
        except ValueError:
            print("Please enter a valid number.")

# Find minimum and maximum
min_value, max_value = find_min_max(numbers)

# Print results
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")
