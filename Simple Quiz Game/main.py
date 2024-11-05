#John Wangwang ProficiencyTest: Simple Quiz Game

questions = ['Whta']
choices = []
answers = ['A', ]

def check(number, answer):

    if answer[number] == answer:
        return True
    else:
        return False

def main():
    print("CHEMISTRY Quiz")

    for (question, choice) in zip(questions, choices):
        print(f"{question}\n{choice}")

        answer = input("Enter your ")

        if check(answer):
            continue
        else:
            

