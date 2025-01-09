# Write a program to find the grade of a student when grades are allocated as given in the table below.
# Programming Exercises - 10

def get_grade(percentage):
    if percentage > 90:
        return 'A'
    elif 80 <= percentage <= 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'E'

def main():
    try:
        # Input percentage from user
        percentage = float(input("Enter the percentage of marks obtained by the student: "))
        
        # Validate input
        if percentage < 0 or percentage > 100:
            print("Please enter a valid percentage between 0 and 100.")
            return
        
        # Get the grade
        grade = get_grade(percentage)
        
        # Output the grade
        print(f"The grade for the student with {percentage}% marks is: {grade}")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value for the percentage.")

if __name__ == "__main__":
    main()
