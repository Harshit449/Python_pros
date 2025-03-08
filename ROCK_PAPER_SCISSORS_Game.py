import random

Computer_points=0
Player_points=0

while True:

    player_choice=input("enter user choice (Rock/paper/scissors):".lower())
    
    computer=random.randint(1,3)
    if computer==1:
        computer_choice='rock'
    elif computer==2:
        computer_choice='paper'
    else:
        computer_choice='scissors'

    

    print(f"Computer choose : {computer_choice},  And Player Choose: {player_choice}".upper())

    if player_choice=='rock' and computer_choice=='rock':
        print("its a DRAW")
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='paper' and computer_choice=='paper':
        print("its a DRAW")
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='scissors' and computer_choice=='scissors':
        print("its a DRAW")
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='scissors' and computer_choice=='rock':
        print("computer wins +1 point")
        
        Computer_points+=1
        Player_points-=1
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='rock' and computer_choice=='paper':
        print("computer wins +1 point")
        Computer_points+=1
        Player_points-=1
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='paper' and computer_choice=='scissors':
        print("computer wins +1 point")
        Computer_points+=1
        Player_points-=1
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='paper' and computer_choice=='rock':
        print("player wins +1 point")
        Player_points+=1
        Computer_points-=1
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='scissors' and computer_choice=='paper':
        print("player wins +1 point")
        Player_points+=1
        Computer_points-=1
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")

    elif player_choice=='rock' and computer_choice=='scissors':
        print("player wins +1 point")
        Player_points+=1
        Computer_points-=1
        print(f"current points of COMPUTER:{Computer_points}   And   Player:{Player_points}")


    if Player_points==3:
        print("player won the Game")
        break
    if Computer_points==3:
        print('computer won the round')
        break
    

