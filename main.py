# score 
score = 0
#ask users name
name=input("what is your name").lower()
#say hello to user and explain the quiz
print("hello" ,name, "this is my quiz")
print("this quiz is about math")
print("dont put any spaces before your answers please")
#ask user a question
answer=input("what is 20 x 35").lower()
#check the answer and tell user
if answer == " 700".lower():
    score += 5
    print("correct the answer is 700 nice job")
else:
    print("silly child this isnt primary school you dummy you should know the anwer is 700")
question = "what is 270 x 32"
a = "8640"
b = "6520"
c = "8600"
d = "6640"
answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).lower()
if answer == a or answer == "a":
    print("nice you got it correct")
    score += 20
elif answer == "":
    print("that is not an answer")
elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer !="d":
    print("that is not an answer")
else:
    print("haha u got it wrong")
#end
print("this is the end thanks for playing {}." .format(name))
print("your final score is", score)