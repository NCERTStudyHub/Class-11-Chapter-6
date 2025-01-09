# Write a program to find the sum of digits of an integer number, input by the user.
# Programming Exercise - 7

def sum_of_digits(number):
    # Convert the number to its absolute value to handle negative numbers
    number = abs(number)
    total_sum = 0
    
    while number > 0:
        digit = number % 10  # Get the last digit
        total_sum += digit    # Add it to the total sum
        number //= 10         # Remove the last digit
    
    return total_sum

# Get user input
try:
    user_input = int(input("Enter an integer number: "))
    result = sum_of_digits(user_input)
    print(f"The sum of the digits of {user_input} is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
