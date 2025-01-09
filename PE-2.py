# Programming Exercises - 2
# Write a function to print the table of a given number. The number has to be entered by the user.

def print_multiplication_table(number):
    """Prints the multiplication table for the given number."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):  # Multiplying from 1 to 10
        print(f"{number} x {i} = {number * i}")

# Get user input
try:
    num = int(input("Enter a number to print its multiplication table: "))
    print_multiplication_table(num)
except ValueError:
    print("Please enter a valid integer.")
