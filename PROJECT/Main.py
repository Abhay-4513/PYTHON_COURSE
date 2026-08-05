'''
ROCK = 1 / r
Paper = 0 / p
Scissors = -1 / S
'''

import random 
import playsound
def game():
    print("================================================")

    print("This is Rock , Paper or Scissors game ")
    print("r = Rock\n" \
    "p = Paper\n" \
    "s = Scissors")

    print("================================================")

    user_wins = 0
    computer_wins = 0
    draws=0
    print("Hello")
    n = int(input("How many rounds you want to play : "))

    print("================================================")

    for i in range(1,n+1): 
        user = input("Enter your choice : ")
        computer = random.choice([1,0,-1])

        gameDict = {"r":1,"p":0,"s":-1}
        reverseDict = {1:"Rock",0:"Paper",-1:"Scissors"}
        you = gameDict[user]

        print(f"You choose : {reverseDict[you]}\nComputer choose : {reverseDict[computer]}")
        # Below is the logic behind the upper calculations....

        if (you - computer  == -1) or (you - computer  == 2):
            print("You won the game.....")
            user_wins +=1
        
        elif computer == you :
            print("It's a draw...")
            draws +=1
        else :
            print("Computer won the game !!")
            computer_wins +=1
            playsound.playsound("fahhh_KcgAXfs.mp3")

#-------------------This is the logic part ,which is later converted into small part------------------------
        # if computer == you:
        #     print("It's a draw")
        #     draws += 1
 
        # else:
        #     if (you == 1) and (computer == 0):
        #         print("Computer Won")
        #         computer_wins +=1
        #     elif (you == 1) and (computer == -1):
        #         print("You Won")
        #         user_wins += 1
            
        #     elif (you == 0) and (computer == 1):
        #         print("You won")
        #         user_wins += 1
        #     elif (you == 0) and (computer == -1):
        #         print("Computer won")
        #         computer_wins +=1
            
        #     elif(you == -1) and (computer == 1):
        #         print("Computer won")
        #         computer_wins +=1
        #     elif(you == -1) and (computer == 0):
        #         print("You won")
        #         user_wins += 1

        #     else:
        #         print("Enter correct choice...")

    print("================================================")

    print(f"Computer won : {computer_wins} rounds\nYou won : {user_wins} rounds\nDraws : {draws}")

    print("================================================")

    if computer_wins > user_wins:
        print("Computer won the game .......")
    elif computer_wins < user_wins:
        print("You won the game .......")

    else:
        print("Its' a draw")
    print("================================================")   

game()
