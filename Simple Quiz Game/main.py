#John Wangwang ProficiencyTest: Simple Quiz Game

questions = [
    {"question" : "What season does Australia experience in December?",
     "options" : "A)Falls\nB)Winter\nC)Summer\nD)Raining",
     "answer" : "C"},
     {"question" : "How many countries are there in the United Kingdom??",
     "options" : "A)4\nB)3\nC)1\nD)2",
     "answer" : "A"},
     {"question" : "What is the capital of Senegal?",
     "options" : "A)Bangkok\nB)Dakar\nC)New York\nD)Vanilla",
     "answer" : "B"},
     {"question" : "How many time zones does Russia have?",
     "options" : "A)5\nB)8\nC)11\nD)13",
     "answer" : "C"},
     {"question" : "What country does the Rhine River run through?",
     "options" : "A)United States\nB)Italy\nC)Egypt\nD)Germany",
     "answer" : "D"}
]
easy_questions = [
    {"question" : "What is the name of the tallest mountain in the world?",
     "options" : "A)Aconcagua\nB)Denali\nC)Mount Everest\nD)Mount Kilimanjaro",
     "answer" : "C"},
     {"question" : "Which country has the largest population in the world?",
     "options" : "A)United States\nB)India\nC)China\nD)Mexico",
     "answer" : "B"},
     {"question" : "What is the name of the longest river in Africa?",
     "options" : "A)The Nile River\nB)Zarima River\nC)Ferrey River\nD)Kidane Mihret River",
     "answer" : "A"},
     {"question" : "What American city is the Golden Gate Bridge located in?",
     "options" : "A)Ohio\nB)Alaska\nC)Texas\nD)San Francisco",
     "answer" : "D"},
     {"question" : "What is the capital of Mexico?",
     "options" : "A)New York\nB)Mexico City\nC)Rome\nD)Vanilla",
     "answer" : "C"},
]

def main():

    score = 0

    print("Geography Quiz!")

    for (question, easy_question) in zip(questions, easy_questions):

        print(f"{question["question"]}\n{question["options"]}")

        answer = input("Enter your answer: ").upper()

        if answer == question["answer"]:
            print("You got the answer right!")
            score += 1
            continue
        else:
            print("You got the answer wrong.\nHere is the easier question!")
            print(f"{easy_question["question"]}\n{easy_question["options"]}")

            answer = input("Enter your answer: ").upper()
            
            if answer == easy_question["answer"]:
                print("You got the answer right!")
                score += 1
                continue
            else:
                print("You still got the answer wrong :(\nMove on to next questions")
                continue
    
    print(f"The quiz ended!\nYou got {score} out of 5!")

if __name__ == "__main__":
    main()