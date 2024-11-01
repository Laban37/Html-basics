subjects = {}
total = 0

try:
    noOfSubjects = int(input("Enter number of subjects: "))
except ValueError:
    print("The number of subjects must be an integer")
    exit()

for i in range(1, noOfSubjects + 1):
    name = input(f"Enter the name of subject {i}: ")

    while True:
        try:
            marks = int(input(f"Enter the marks of subject {i}: "))
            if 0 <= marks <= 100:
                break
            else:
                print("The marks should be between 0 and 100.")
        except ValueError:
            print("The marks should be an integer.")

    subjects[name] = marks
    total += marks

average = total / len(subjects)
subjects["total"] = total
subjects["average"] = int(average)

print(subjects)









