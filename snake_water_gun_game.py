# SNAKE WATER GUN GAME
"""
snake - water = sanke wins
water - gun = water wins
snake - gun = gun wins
you hv to ask user to enter theiir chice , gnrt computer's choice and compare
you hv to declare winner from 10 chances and display how mny times u win and how mny times computer wins
"""
import random
list_of_choices=["snake","water","gun"]
your_score=0
computers_score=0

def play_game(user_choice,random_choice):
    global your_score
    global computers_score
    #if (user_choice!='snake' or user_choice!='gun' or user_choice!='water'):
      #  print("enter valid choice")
    #else:
    if (user_choice == 'snake' and random_choice == 'water') or (user_choice=='water'and random_choice=='gun') or (user_choice=='gun'and random_choice=='snake'):
        print("You win this round!!")
        your_score += 1
            #print(your_score)
    elif (user_choice==random_choice):
        print("Tie!!")
        #your_score+=1
        #computers_score+=1
    else:
        print("you loose this round")
        computers_score+=1

print("Lets Play Game:\nRules:snake - water = sanke wins\nwater - gun"
      " = water wins\nsnake - gun = gun wins")

i=0

while(i<10):

    i+=1
    print("Enter your choice:")
    user_choice = str(input())
    if(user_choice=="snake" or user_choice=="gun" or user_choice=="water"):
        random_choice = str(random.choice(list_of_choices))
        print(random_choice)
        play_game(user_choice,random_choice)
    else:
        print("wrong input please enter correct choice")

if computers_score>your_score:
    print(f"You Lost The Game!!\nYour final score:{your_score}\nComputer final score:{computers_score}")
elif computers_score==your_score:
    print(f"This game is Tie!!\nYour final score:{your_score}\nComputer final score:{computers_score}")
else:
    print(f"You win!!\nYour final score:{your_score}\nComputer final score:{computers_score}")

input()
