def welcome():
  print("""Hello and welcome to an adventure/survival quiiizzz!, in this quiz we will test your ability to think in desperate situations!!! 
***********************************************************************************
Here are some basic things you should know before you start your quiz! 
***********************************************************************************
For every question you get correct you will earn a point!!!these points add up and determine your level of intelligence!!how good are you are at surviving!!! 
***********************************************************************************
there are possibilaties where you can end this quiz in a shorter ammount of time!!
***********************************************************************************
this may happen because you pick the wrong option and end up un-survivinggg! 
**********************************************************************************
when this happens you will be taken back to the start of the quiz!!enjoyyy!!!
***********************************************************************************
""")

def name():
  print("Please only enter name in letters")
  while True:
        name = input("please enter your name to begin: ")
        if name.isalpha():
          break 
        else:
          print("Please only enter name in letters")
      
  print("Hello " + name) 
  print("""lets begin!!
        
      """)




def questions():
  global score
  
questionss = { 'Question 1 :  you wake up, take off your seat belt,stand up and see hundreds of people sleeping,what do you do? \n \n a: look around for anyone that is awake \n \n b: go back to sleep \n \n c: get out the aircraft and see the surroundings\n' : 'a' , 
         
'Question 2 : you go look around to see if anyone is still alive , and by some miracle you find someone that was looking for any survivor too! yaaay you found someone!!now what should you and your fellow survivor do? \n  \n a: get out the aircraft,check surroundings \n \n b: look around inside the plane for anything that can prove usefull e.g food, warm clothes/blankets etc \n\n c: send the survivor to sleep.  \n' :  'b' , 
             
'Question 3 : you and your fellow survivor look around the plane and find plenty of extra warm clothes blankets etc. you and your fellow survivor have luckily aready been fed during the in flight meals, what should you and your do next? \n\n a: look out the window to see surrondings,where you are. \n\n b: stab your fellow survivor in the back, basicaly un alive him,you dont need him no more. \n\n c: watch a movie and chill \n \n' : 'a' }

def run_quiz():
  for key in questionss.keys():
    user_answer=input(key).lower().strip()
    if questionss.get(key)==user_answer:
        print("Correct! \n ") 
     
    else:
        print("You're Wrong! the correct answer is " + questionss.get(key) + "\n" )


# Start of program
welcome()
name()
questions()
run_quiz()



