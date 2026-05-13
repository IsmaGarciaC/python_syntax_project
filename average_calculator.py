def enter_grades():
    
    subjects = [] #List for subjects
    grades = [] # List for grades
    
    print("Schoolar Calculator\n")

    while True:
        subject = input("Enter Subject: ")

        while True:
            try:
                grade = float(input("Enter a new grade between 0 and 10: "))

                if 0 <=  grade <= 10: #Checking if the grade is valid
                    break
                else:
                    print("Error: The grade must be between 0 and 10.")
            
            except ValueError:
                print("Error: Invalid input. Please enter a numerical value.")

            #Add the values to the list
        subjects.append(subject)
        grades.append(grade)

        state = input("Would you like to keep uploading grades? (yes/no): ").lower()
        if state == "no":
            break
                
    return subjects, grades

def calculate_average(grades):
    average_grade = sum(grades) / len(grades) # The formula
    return average_grade

def determine_status(grades, threshold = 5.0):
    #Create the two lists
    passed = [] 
    failed = []

    #Loop the list, checking every index
    for index, grade in enumerate(grades):
        if grade < threshold:
            failed.append(index)
        else:
            passed.append(index)
    return passed, failed

def find_extremes(grades):
    high = grades.index(max(grades))
    low = grades.index(min(grades))
    return high, low

def main():
    subjects, grades = enter_grades()

    if not subjects:
        print("No subjects found.")
    else:
        average = calculate_average(grades)
        passed, failed = determine_status(grades)
        highest, lowest = find_extremes(grades)

        print("\n---------------------------")
        print("SUMMARY")
        #Show subjects
        for i in range(len(subjects)):
            print(f"Subject: {subjects[i]} | Grade: {grades[i]}")
        
        #Show average
        print(f"\nOverall Average: {average:.2f}")

        #Show passed and failed subjects
        print(f"Passed subjects: {[subjects[i] for i in passed]}")
        print(f"Failed subjects: {[subjects[i] for i in failed]}")

        #Show highest
        print(f"Highest grade: {grades[highest]} in {subjects[highest]}")
        print(f"Lowest grade: {grades[lowest]} in {subjects[lowest]}")
    
    print("---------------------------")
if __name__ == "__main__":
    main()