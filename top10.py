import random

score = 0
MAX_TURNS = 10

#welcome to quiz
def intro():
    #name
    name = input("what is your name")

    #hello user
    print("welcome to my quiz,",name)
    print("this quiz is about the top ten most streamed songs have fun ;)")
    
def getpassword():
    while True:
        password = input("what is the password")
        if password == "hehe":
            return
        else:
            print("wrong answer try again")
def getnumber():
    number = input("give me number")
    return int(number)

number = getnumber()
print(number)

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
            
#---------functions----------
def addfive(number):
    return number + 5

#---------main code----------
num = addfive(14)
intro()
lives = getlives()
tries = getnumber()
SS_ANSWERS = []