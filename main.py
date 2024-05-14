score = 0
play=input("do you want to play my quiz")
while play == "yes":

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
   question_attempts = tries
   while question_attempts > 0:
   
      answer=input("what is 20 x 35").lower()
      #check the answer and tell user
      if answer == "700".lower():
         score += 5
         print("correct the answer is 700 nice job")
         break
      else:
         print("silly child this isnt primary school you dummy you should know the anwer is 700")

      question_attempts -=1


   while question_attempts > 0:
      question = "what is 270 x 32"
      a = "8640"
      b = "6520"
      c = "8600"
      d = "6640"
      answer = input("{}\nA.{} B.{} C.{} D.{}".format(question, a, b, c, d)).lower()
      if answer == a or answer == "a":
         print("nice you got it correct")
         score += 20
         break
      elif answer == "":
         print("that is not an answer")
      elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer !="d":
         print("that is not an answer")
      else:
         print("haha u got it wrong silly billy")
      question_attempts -= 1
   #end
   print("this is the end thanks for playing {}." .format(name))
   print("your final score is", score)
   
   play = input("do you want to play again")
   print("thanks for playing")