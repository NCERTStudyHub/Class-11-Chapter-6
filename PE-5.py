# Write a program to generate the sequence: –5, 10, –15, 20, –25….. upto n, where n is an integer input by the user.
# Programming Exercises - 5

def generate_sequence(n):
    sequence = []
    for i in range(1, n + 1):
        # Calculate the term based on the index
        term = (-1) ** i * (5 * i)
        sequence.append(term)
    return sequence

# Get user input
try:
    n = int(input("Enter an integer value for n: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = generate_sequence(n)
        print("Generated sequence:", result)
except ValueError:
    print("Invalid input. Please enter an integer.")
