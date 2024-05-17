import random

Q_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
GOOD_COMMENTS = ["horray", "good job", "GREAT"]
BAD_COMMENTS = ["bad", "try again", "get good then have another try"]
QUESTIONS = ["what is 20 x 35", 
                   "what is 270 x 32"]
OPTIONS = [["700","670","770","600"],
                 ["8640","6520","8600","6640"]]
SHORT_OPTIONS = ["a","b","c","d"]
ANSWERS = [0,0,0]





play=input("do you want to play my quiz")
while play == "yes":
   score = 0
   # score 
   
   
   #try
   while True:
      try:
         tries = input("how many attempts would you like for each question 1-4")
         tries = int(tries)
         break
      except:
         print("thats not a answer")

   
   #ask users name
   name=input("what is your name").lower()
   
   
   #say hello to user and explain the quiz
   print("hello" ,name, "this is my quiz")
   print("this quiz is about math")
   print("dont put any spaces before your answers please")
   
  
   #ask user a question
   answer = input(Q_FORMAT.format(QUESTIONS[0],OPTIONS[0][0],
                                   OPTIONS[0][1], OPTIONS[0][2], OPTIONS[0][3])).lower()
   
   if answer == OPTIONS[0][ANSWERS[0]] or answer == SHORT_OPTIONS[ANSWERS[0]].lower():
      print("yippie")
   elif answer in SHORT_OPTIONS or answer in OPTIONS[0]:
      print("wrong")
      print(random.choice(BAD_COMMENTS))
   else:
      print("that wasnt an option")
   
   
   
   question_attempts = tries
   while question_attempts > 0:   
       
      
   
   #end
      print("this is the end thanks for playing {}." .format(name))
      break
   print("your final score is", score)
   
   play = input("do you want to play again")
   print("thanks for playing")
   
  