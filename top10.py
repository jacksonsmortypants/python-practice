guesses = []
SS_ANSWERS = ["blinding lights","shape","someone you loved","sunflower","starboy","as it was","one dance","stay","dance monkey","beliver"]

score = 0
MAX_TURNS = 10

#welcome to quiz
def intro():
    #name
    name = input("what is your name")

    #hello user
    print("welcome to my quiz,",name)
    print("this quiz is about the top ten most streamed songs have fun ;)")

def getlives():
    while True:
        lives = input("how many attempts would you like")
        try:
            lives = int(lives)
            if lives >= 0:
                return lives
            else:
                print("a positive number please")
        except:
            print("that is not a number")

def inlist(answer, list):
    if answer in list:
        return True
    else:
        return False
            

#---------main code----------
intro()
lives = getlives()

while lives > 0:
    answer = input("name one of the top ten most streamed songs on spotify:\n").lower()
#correct or wrong
    if inlist(answer, SS_ANSWERS):
        if inlist(answer, guesses):
            print("you have got that already")
        else:
            print("correct")
            score += 5
            guesses.append(answer)
            print("you have guessed{}. your score is {}. you have {} chances remaining". format(len(guesses),score,lives))
    else:
        print("wrong")
        lives -= 1
        print("you have guessed{}. your score is {}. you have {} chances remaining". format(len(guesses),score,lives))
    if score == 50:
        print("well done")
        break



print("game over nice")     