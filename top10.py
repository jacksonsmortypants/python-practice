import random

score = 0
MAX_TURNS = 10
#---------functions----------

#welcome to quiz
def intro():
    #name
    name = input("what is your name")

    #hello user
    print("welcome to my quiz,",name)
    print("this quiz is about the top ten  have fun ;)")\
    
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
#---------main code----------

intro()
lives = getlives()
tries = getnumber()
BN_ANSWERS = []