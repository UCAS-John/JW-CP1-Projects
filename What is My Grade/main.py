#John Wangwang SkillPractice: What is My Grade

def grade(grade: float):
    """
    Get in grade percentage as a parameter
    return false if percentage is out of range
    return the letter grades
    """
    if grade > 100 or grade < 0:
        return False
    elif grade >= 94:
        return "A"
    elif grade >= 90: 
        return "A-"
    elif grade >= 87: 
        return "B+"
    elif grade >= 84: 
        return "B"
    elif grade >= 80:
        return "B-"
    elif grade >= 77: 
        return "C+"
    elif grade >= 74: 
        return "C"
    elif grade >= 70: 
        return "C-"
    elif grade >= 67:
        return "D+"
    elif grade >= 64: 
        return "D"
    elif grade >= 60:
        return "D-"
    else:
        return "F"
    
def main():

    Letter = list()
    Name = list()
    
    while True:
        class_name = input("Enter your class name: ") #Get class name

        try:
            percent_grade = float(input("Enter your grades percentage: ")) #Get grade percentage
        except ValueError:
            print("\nPlease type in Valid percentage\n")
            continue

        letter_grade = grade(percent_grade)

        if letter_grade == False:
            print("\nGrade out of range. Please enter again.\n")
            continue
        
        Letter.append(letter_grade)
        Name.append(class_name)

        #ask user for choice
        choice = input("""\nType any key to continue enter your grade
type 1 to print out your grade book
Enter your choice: """)
        
        if choice == "1":
            print("")
            break
    
    #Print out classname and grade 
    for name, letter in zip(Name, Letter):
        print(f"Your letter grade of {name} is {letter}.")

if __name__ == "__main__":
    main()