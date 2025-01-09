# Programming Exercise - 1
# Write a program that takes the name and age of the user as input and displays a message whether the user is eligible to apply for a driving license or not. (the eligible age is 18 years).

# Get user input for name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert age to an integer

# Check eligibility for a driving license
if age >= 18:
    print(f"{name}, you are eligible to apply for a driving license.")
else:
    print(f"{name}, you are not eligible to apply for a driving license.")
