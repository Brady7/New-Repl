# first_name=input ("What is your first name?")
# last_name=input ("What is your last name?")
# print (""+ last_name + first_name)

# numbers=[1,2,3,4,5]
# print (numbers)
# sum=0
# for numbers in range (1,6):
#   sum=(sum+numbers)
# print (sum)
# ----------------------------------------------------------

# # bells=0
# # if bells>=5000:
# #   print ("I can pay off Tom Nook!")
# # else: 
# #   print("I cannot pay off Tom Nook.")

# season=input ("What is the season? Enter Spring, Summer, Fall or Winter.") 
# if season=="spring" or season=="Spring":
#   print ("Plant trees!")
# elif season=="summer" or season=="Summer":
#  print ("Water trees!")
# elif season=="fall" or season=="Fall": 
#   print ("Pick apples from the trees!")
# elif season=="winter" or season== "Winter":
#   print ("Stay inside instead of doing anything to the trees!")
# else:
#   print ("That's not a season!")



import random
computerNumber=random.randint(0,10)
NumberofTries=7
Play=True
Win=False
print (computerNumber)
while Play==True:
  while NumberofTries>0:
   PlayerNumber=input ("Choose a number between 1 and 10:")
   PlayerNumber=int(PlayerNumber)
   if PlayerNumber>10 or PlayerNumber<0:
     print ("Bad Number.That's not between 1 and 10!")
     break
   else:
      if PlayerNumber < computerNumber:
        print ("Number too low!")
        NumberofTries=NumberofTries-1
        print ("You have",NumberofTries," tries remaining.")
      elif PlayerNumber > computerNumber:
        print ("Number too high!")
        NumberofTries=NumberofTries-1
        print ("You have",NumberofTries,"tries remaining.")
      else:
        if PlayerNumber==computerNumber:
          print ("Correct Number!")
          Win=True
          break
  if Win==True:
    print ("Congratulations!")
  else:
    print ("You're out of tries!")
    print ("The correct number was",computerNumber,".")
  UserAnswer=input ("Do you want to play again?")
  if UserAnswer=="y" or " y":
    Win=False
    NumberofTries=7
  else:
    print ("Bye!")
    Play=False
  
    
      
  
        

