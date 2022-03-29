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
    try:
        name = input("please enter your name to begin: ")
        if name.isalpha():
          break
    except ValueError:
        print("Please only enter name in letters")
      
  print("Hello " + name) 
  print("""lets begin!!
        
      """)

score=0
questions = { 'you wake up, take off your seat belt,stand up and see hundreds of people sleeping,what do you do? \n a: look around for anyone that is awake \n b: go back to sleep \n c: get out the aircraft and see the surroundings\n' : 'a' , 'Question 2\n a: answer a\n b: answer b\n c: answer c \n' :  'b' , 
             'Question 3 \n a: answer a\n b: answer b\n c: answer c \n' : 'c' }

def run_quiz():
  for key in questions.keys():
    user_answer=input(key).lower().strip()
    if questions.get(key)==user_answer:
        print("Correct!") 
    else:
        print("You're Wrong!")


# Start of program
welcome()
name()
run_quiz()
 

