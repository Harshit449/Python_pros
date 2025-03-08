player1_Hp=100
player2_Hp=100
p1_mana=5
p2_mana=5
p1_def=False
p2_def=False


def atk(i):
    print(f"player{i} choose normal {player_move.upper()}")
    if i==1:
        global p1_def,p2_def
        if p2_def==False:
            print(f"player  {i} Turn")
            global player2_Hp,p1_mana
            player2_Hp-=15
            p1_mana+=5
            print("player 2 took damage current Hp is :",{player2_Hp})
            print("current mana of player 1:",{p1_mana})
        else:
            print(f"player  {i} Turn")
            player2_Hp-=5
            p1_mana+=2
            p2_def=False
            print("player 2 took damage current Hp is :",{player2_Hp})
            print("current mana of player 1:",{p1_mana})

    else:
        if p1_def==False:
            print(f"player  {i} Turn")
            global player1_Hp,p2_mana
            player1_Hp-=15
            p2_mana+=5
            print("player 1 took damage current Hp is :",{player1_Hp})
            print("current mana of player 2:",{p2_mana})
        else:
            print(f"player  {i} Turn")
            player1_Hp-=5
            p2_mana+=2
            p1_def=False
            print("player 1 took damage current Hp is :",{player1_Hp})
            print("current mana of player 2:",{p2_mana})




def defence(i):
    print(f"player{i} choose {player_move.upper()}")
    global player1_Hp,player2_Hp
    if i==1 and player_move=='def':
        player1_Hp+=5

        print(f"player {i} choose def will recive less damage next atk and recovered some hp current hp {player1_Hp}")
        global p1_def
        p1_def=True
        
    else:
        player2_Hp+=5

        print(f"player {i} choose def will recive less damage next atk and recoverd some hp cureent hp {player2_Hp}")
        global p2_def
        p2_def=True
        
        


def skill(i):
    print(f"player{i} choose {player_move.upper()}")
    if i==1:
        global p1_mana,p2_mana
        if p1_mana>=20:
            global player2_Hp
            player2_Hp-=25
            p1_mana-=20
            print(f"Special Skill used player 2 took damage  and cureent Hp is :{player2_Hp}")
            print("current mana of player 1:",{p1_mana})
        else:
            print("mana not enough wasted a move")
    else:
        if p2_mana>=20:
            global player1_Hp
            player1_Hp-=25
            p2_mana-=20
            print(f"Special Skill used player 1 took damage and current hp is:{player1_Hp}")
            print("current mana of player 2:",{p2_mana})
        else:
            print("mana not enough wasted a move")



while True:
    
    for i in range(1,3):
        if i==1:
            print("cureent mana of Player 1 :",{p1_mana})
        elif i==2:
            print("cureent mana of Player 2 :",{p2_mana})
        

        player_move=input(f"player  {i}  enter The move (def/atk/skill): [mana required for skill 20]  ").lower()
        

        if player_move=='atk' or player_move=='a':
            atk(i)
        elif player_move=='def'or player_move=='d':
            defence(i)
        elif player_move=='skill' or player_move=='s':
            skill(i)
        else:
            print("wrong input")
            continue
    
        if player1_Hp<=0:
            print(f"Player 2 Won the Game")
            break
        if player2_Hp<=0:
            print(f"player 1 Won the Game ")
            break

    break
        

    
        

