print("""Hello and welcome to an adventure/survival quiiizzz!, in this quiz we will test your ability to think in desperate situations!!! 
      ****************************************************
      
Here are some basic things you should know before you start your quiz! 
      *****************************************************
For every question you get correct you will earn a point!!!these points add up and determine your level of intelligence!!how good are you are at surviving!!! 
      
there are possibilaties where you can end this quiz in a shorter ammount of time!!

this may happen because you pick the wrong option and end up un-survivinggg! 
      
when this happens you will be taken back to the start of the quiz!!enjoyyy!!!
      *********************************************************\n""")


while True:
    try:
        name = input("please enter your name: ")
        if name.isalpha():
          break
    except ValueError:
        print("Please only enter name in letters")
      
print("Hello " + name) # or carry on what you want with the integer
