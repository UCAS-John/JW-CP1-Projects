#John Wangwang Graded Quiz

question = [""] * 5
correct = [""] * 5
score = 0

#declare 5 questions
question[0] = """What is the approximate diameter of observable universe?
A. 16 Tillion light-years
B. 76 million light-years
C. 93 billion light-years                                                     
D. 89 billion light-years"""
correct[0] = "C"

question[1] = """Who is the current CEO of OpenAI?
A. Sam Altman
B. Elon Musk
C. Greg Brocman                                                   
D. Bill Gates"""
correct[1] = "A"

question[2] = """Who proved Isaac Newton wrong about his gravity theory?
A. Marie Curie
B. Max Planck
C. Niels Bohr                                                    
D. Albert Einstein"""
correct[2] = "D"

question[3] = """What country has the current highest population?
A. China
B. India
C. United States of America                                                    
D. Indonesia"""
correct[3] = "B"

question[4] = """What year did United States terminated convertibility of the US dollar to gold at a fixed value?
A. 1992
B. 2001
C. 1963                                                     
D. 1971"""
correct[4] = "D"

#loop through each questions and check the answers
for i in range(0,5): 
    print(question[i])
    answer = input("Enter Your answer: ")
    if answer.upper() == correct[i]:
        score += 1

#print total score
print(f"You answer correct {score} questions out of 5 questions.")