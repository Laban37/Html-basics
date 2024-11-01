def calculate_grade(physics, math, kiswahili):
    # Check for negative marks
    if physics < 0 or math < 0 or kiswahili < 0:
        return "Error: Marks cannot be negative."

    # Calculate the average
    total_marks = physics + math + kiswahili
    average = total_marks / 3

    # Check if the average exceeds 100
    if average > 100:
        return "Error: Average exceeds the maximum possible score of 100."

    # Assign grades based on average
    if average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'F'

    return f"Average: {average:.2f}, Grade: {grade}"


# Get user inputs
try:
    physics = float(input("Enter the Physics mark: "))
    math = float(input("Enter the Math mark: "))
    kiswahili = float(input("Enter the Kiswahili mark: "))

    # Display the result
    print(calculate_grade(physics, math, kiswahili))

except ValueError:
    print("Error: Please enter valid numeric marks.")
