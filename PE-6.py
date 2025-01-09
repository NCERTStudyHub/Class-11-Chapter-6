# Write a program to find the sum of 1+ 1/8 + 1/27……1/n3, where n is the number input by the user.
# Programming Exercises - 6

def sum_of_series(n):
    total_sum = 0.0
    for i in range(1, n + 1):
        total_sum += 1 / (i ** 3)
    return total_sum

# Get user input
try:
    n = int(input("Enter a positive integer value for n: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = sum_of_series(n)
        print(f"The sum of the series up to n={n} is: {result:.6f}")
except ValueError:
    print("Invalid input. Please enter an integer.")
