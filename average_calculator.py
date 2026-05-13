def enter_grades():
    
    subjects = [] #List for subjects
    grades = [] # List for grades
    
    print("Schoolar Calculator\n")

    while True:
        subject = input("Enter Subject: ")
        grade = float(input("Enter a new grade between 0 and 10: "))

        while grade < 0 or grade > 10:
            print("Error: The grade must be between 0 and 10.")
            grade = float(input("Try again. Enter grade: "))
        subjects.append(subject)
        grades.append(grade)

        state = input("Would you like to keep uploading grades? (yes/no): ")
        if state == "no":
            break

    return subjects, grades

