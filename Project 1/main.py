'''
-1 - rock
0 - paper
1 -  scissor


'''
import random

computer = random.choice([-1,0,1])
youIn = input("Enter your choice(R,P,S): ")
youDict = {"R" : -1,"P" : 0,"S" : 1}
reverseDict = {-1:"ROCK",0:"Paper",1:"Scissor"}
you = youDict[youIn]
print(f"You choose {reverseDict[you]} - Computer Choose {reverseDict[computer]}")
result = computer - you

if(computer == you):
    print("It's a Draw!")
# else:
#     if(computer ==-1 and you ==1): -2
#       print("You lose!")
#     elif(computer ==-1 and you==0):-1
#       print("You won!")
#     elif(computer == 0 and you ==-1):1
#       print("You lose!")
#     elif(computer == 0 and you==1):-1
#       print("You win!")
#     elif(computer == 1 and you == -1):2
#       print("You win!")
#     elif(computer== 1 and you== 0):1
#       print("You lose!")
#     else:
#       print("Something went wrong!")
else:
    if(result == -2 or result == 1 ):
      print("You Lose!")

    elif(result == -1 or result == 2):
       print("You Won!")
    else:
       print("Something went wrong!")


    


