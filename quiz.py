print('Welcome to Imeldas Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language? ')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 2: Are you a student at igs? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: what is imeldas age? ')
    if answer.lower()=='15':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

else:
    print('Okay, Goodbye')

print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')