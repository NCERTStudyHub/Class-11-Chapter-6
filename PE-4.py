# Write a program to check if the year entered by the user is a leap year or not
# Programming Exercise - 4

def is_leap_year(year):
    """Returns True if the year is a leap year, False otherwise."""
    # A year is a leap year if:
    # 1. It is divisible by 4
    # 2. If it is divisible by 100, it must also be divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get user input
try:
    year = int(input("Enter a year: "))  # Accepting input as an integer
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Please enter a valid integer for the year.")
  
