def enter_grades():
    
    subjects = [] #List for subjects
    grades = [] # List for grades
    
    print("Schoolar Calculator\n")

    while True:
        subject = input("Enter Subject: ")
        grade = float(input("Enter a new grade between 0 and 10: "))

        while grade < 0 or grade > 10: #Checking if the grade is valid
            print("Error: The grade must be between 0 and 10.")
            grade = float(input("Try again. Enter grade: "))
        
        #Add the values to the list
        subjects.append(subject)
        grades.append(grade)

        state = input("Would you like to keep uploading grades? (yes/no): ")
        if state == "no":
            break

    return subjects, grades

def calculate_average(grades):
    average_grade = sum(grades) / len(grades) # The formula
    return average_grade

def determine_status(grades, threshold = 5.0):
    passed = []
    failed = []

    for index, grade in enumerate(grades):
        if grade < threshold:
            failed.append(index)
        else:
            passed.append(index)
    return passed, failed

