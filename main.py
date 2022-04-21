#component 1: welcomes users to my survival quiz and give instructions
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

#component 2: this function asks fo th3e name, checks its alpha 
  #it has a while loop so it keeps asking untill user enters a letter
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

#component 3, quiz running questions, all questions and answers stored as key in a dictionary, the value is the correct choice
def questions():
  global score
  
questionss = { 'Question 1 :  you wake up, take off your seat belt,stand up and see hundreds of people sleeping,what do you do? \n \n a: look around for anyone that is awake \n \n b: go back to sleep \n \n c: get out the aircraft and see the surroundings\n' : 'a' , 
         
'Question 2 : you go look around to see if anyone is still alive , and by some miracle you find someone that was looking for any survivor too! yaaay you found someone!!now what should you and your fellow survivor do? \n  \n a: get out the aircraft,check surroundings \n \n b: look around inside the plane for anything that can prove usefull e.g food, warm clothes/blankets etc \n\n c: send the survivor to sleep. \n \n' :  'b' , 
             
'Question 3 : you and your fellow survivor look around the plane and find plenty of extra warm clothes blankets etc. you and your fellow survivor have luckily aready been fed during the in flight meals, what should you and your do next? \n\n a: look out the window to see surrondings,where you are. \n\n b: stab your fellow survivor in the back, basicaly un alive him,you dont need him no more. \n\n c: watch a movie and chill \n \n' : 'a' ,
             
             
'Question 4 : you and your fellow survivor look out the window and look to see that you are in the middle of no where in an undiscovered island.you and your fellow survivor open the door and get off the plane to see the surroundings and oh no! you fellow survivor gets attacked buy some lionish looking creature!you look around to see if there is anything u can use to kill/ get rid of the lion and you have 2 things infront of you, what should you use? \n\n a: a butter knife you got from the plane. \n\n  b: run away, save your self. \n\n c: sprint back in the plane,grab some leftover meat/bones and try feed/throw it to the lion to distract it. \n\n d: run barehandedly and try bash up the lion with your bare hands. \n\n' :'c' , 
             
 'Question 5 : you grap some leftover meat and feed/throw it to the lion , the lion that is starving gets distracted and enjoys his ecconomy class meal , your fellow survivor thanks you for saving him and oh no! the lion has finished its meal!! it now aproaches and oh! it started licking us in a way of thanks??!! we have now gained a new ally! the lion then starts to gently grab you, as in to follow him,what should you do? \n\n a:follow the lion. \n\n b:dont follow the lion do your own thing. \n\n'  :'a' ,
             
 'Question 6 : you follow the lion through the jungle and it takes you to a what seems like and abandoned treehouse, you and your fellow survivor decide to explore the treehouse and look for anything usefull,anything that can help you survive, find out where you are and hyow to get back home, you find a map of the island itself made from the previos person the used to live there with a bunch of symbols showing a boat on the corner of the island, a house in which where you are and a symbol that seems to be worn out/ un-recognisable, where should you and your fellow survivor head to? \n\n a: head to the unrecogisable symbol,take the risk\n\n b: stay in the treehouse, settle in \n\n c: head towards the boat symbol \n\n' :'c', 
             
'Question 7 : you and your fellow survivor head towards the boat symbol and after long hours you finaly reach your destination, and infront of you,you have a boat, but there is a little bit of an issue.... the boat can only take one person at a time and only has fuel for one trip,knowing this your fellow survivor backstabs you and quickly attemts to take the boat for him self, what should you do??? \n\n a: quickly run, jump on him and start trying to beat him up\n\n b:you may not have much time but you attempt to run,grab the nearest stick and attempt to destroy the boat.\n\n  c:you may not have much time but try to quickly grab a large stick and attempt to remove him from existence.\n\n'  :'c',     
             
'Question 8 : you quickly run to grab a large stick,luckily there was one nearby, but it still took a bit of time, you sprint back to see you fellow survivor attempting to pull start the boat, luckily the boat engine was cold and was not turned on in a while and could not start 1st try, you aproach him and you swing but he doges!! you attempt to swing again , in attempt to doge he slips of the boat and falls in the water!! what should you do????!!!\n\n a:drown him, jump on him and make sure his head stays underwater. \n\n  b: quickly hop on the boat while you can and try starting it so u can leave asap.\n\n' :'a'}

#This is the mechanism that loops through each key in the dictionary, then checks the user input against the value for that key and compares if its correct or incorrect
def run_quiz():
  score=0
  for key in questionss.keys():
    user_answer=input(key).lower().strip()
    if questionss.get(key)==user_answer:
        score+=1
        print(" Correct! your score is " + str(score) + " \n\n  ") 
     
    else:
        print("You're Wrong! the correct answer is " + questionss.get(key) +  " your score is" + str(score) + "\n" )

#this function just prints to the console the last message after quiz ends
def end(): 
  print ('you quickly jump ontop of him and shove his head in the water making sure it stays there, your fellow traitor struggles as u drown him and boink!! the traitor has grabbed your stick and wacked it on your head, you then fall of him as he starts to drown you back, as you are about to pass out something aproaches... your fellow lion thing!!!!?!?!?! it has remembered your kindness and has come to you back for it!!! the lion quickly comes and dispose of the traitor. the traitor is now gone,there is nothing left but you,the lion and the boat,you give the lion a freindly chin scratch as you prepare the boat and leave.you are sad you have to leave the fellow lion but it is what is is. you grab the compass you found on your boat,head south east, eat some rotting plane food and finaly arive home. the end')


#I added all previous functions to just one main function to tidy up the whole quiz
def main():
  welcome()
  name()
  questions()
  run_quiz()
  end()

# Start of program all functions run through one main function only
main()



