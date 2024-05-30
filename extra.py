name = input("hello what is your name")
print("hi",name)
play = input("would you like to play my game")
if play == "yes":
    print("good")
else:
    print("to bad you will play anyway")
print("in my game we will both guess a number from 1-3 if the numbers are the same you win if they are different i win")

while True:
    number = input("say a number from 1-3")
    if number == "1":
        print("my number is 2 i win hahaha")
    elif number == "2":
        print("my number is 3 i win hahaha")
    elif number == "3":
        print("my number is 17 i win hahaha")
    else:
        print("you cant do that")