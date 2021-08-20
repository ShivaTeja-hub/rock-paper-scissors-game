
import random
print("rock.......")
print("paper......")
print("scissor....")

print("do you want to play with other player or with computer ")
number_of_players=int(input("please select 1 or 2 "))
if number_of_players>2:
    print("you selected rather than 1 or 2you must selectonly 1 or 2 " )
    print("you select once again ")
    number_of_players=int(input("please enter number now between 1 or 2"))
    if number_of_players>2:
        print("invalid input")
        exit

if number_of_players==1:
    player0=input("enter the first player name  ")
    player=input(player0+" make your move  ")

    rand_num=random.randint(0,2)
    if rand_num==0:
        computer="rock"
    elif rand_num==1:
        computer="paper"
    else :
        computer="scissor"
    print("computer choses  "+computer)
    
    if player==computer:
        print("its a tie  ")
    elif player=="rock":
        if computer=="scissor":
            print(player0 +" wins")
        elif computer=="paper":
            print("computer  wins")

    elif player=="paper":
        if computer=="rock":
            print(player0 +" wins")
        elif computer=="scissor":
            print("computer wins")
    elif player=="scissor" :
        if computer=="paper":
            print(player0 +" wins")
        elif computer=="rock":
            print("computer wins")
    else:
        print("someting went wrong  ") 

elif number_of_players==2:
    print("enter the players name  ")
    player01=input("enter player 1 name  ")
    player02=input("enter player 2 name  ")
    player1=input(player01+" "+" make your move  ")
  #  print("no cheatring\n"*10)
    player2=input(player02+" " +" make your move  ")

        
    if player1==player2:
        print("its a tie")
    elif player1=="rock":
        if player2=="scissor":
            print(player01 +" wins")
        elif  player2=="paper":
            print(player02 +" wins")

    elif player1=="paper":
        if player2=="rock":
            print(player01 +" wins")
        elif player2=="scissor":
            print(player02 +" wins")

    elif player1=="scissor" :
        if player2=="paper":
            print(player01 +" wins")
        elif player2=="rock":
            print(player02 +" wins")

    else:
        print("someting went wrong")          