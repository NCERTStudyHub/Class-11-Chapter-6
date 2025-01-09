# Write a function that checks whether an input number is a palindrome or not.
# Programming Exercises - 8

def is_palindrome(number):
    # Convert the number to a string to check for palindrome
    str_number = str(number)
    # Check if the string is equal to its reverse
    return str_number == str_number[::-1]

# Get user input
try:
    user_input = int(input("Enter an integer number: "))
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome.")
    else:
        print(f"{user_input} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter an integer.")
