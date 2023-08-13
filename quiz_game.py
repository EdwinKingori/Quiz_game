def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------")
        print (key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A,B,C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#---------------------
def display_score(correct_guesses, guesses):
    print("#------------------------")
    print("RESULTS")
    print("#------------------------")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end =" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end =" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print(f" Your scote is:  {str(score)}" +"%") 



    
#---------------------
def play_again():
    response = input("Do you want to play again?: ")
    response.upper()

    if response == "yes":
        return True
    else:
        return False
    
#---------------------

questions ={
    "Who was the first man to orbit space?": "A",
    "Who created python?":  "B",
    "Python is tributed to which comedy group?" : "C",
    "Is Earth round? ": "B"
}

options = [["A. Yuri A. Gagarin", "B. Neil Armstrong", "C. Virgil Grissom", "D. Gherman Titov"],
["A. Elon Musk", "B. Guido Van Rossum", "C. Bill Gates", "D. Steve Jobs"],
["A. A lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
["A. False", "B: True", "C. Not Sure"]]

new_game()

while play_again():
    new_game()

print("Bye!")