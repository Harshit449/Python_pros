import random

class The:
    
    def __init__(self):
        self.total_tressure=0
        self.player_hp=100


    def tres(self):
        if self.total_tressure<=0:
            self.total_tressure=0
        self.total_tressure+=3
        
        if self.player_hp<100:
            self.player_hp+=5
            print(f"got 3 tressures now the total tresuures are {self.total_tressure} + Hp gained {self.player_hp} ")
        else:
            print(f"got 3 tressures now the total tresuures are {self.total_tressure} + Hp gained {self.player_hp} ")

        


    def trap(self):
        if self.total_tressure>=0:
            self.total_tressure-=2
            self.player_hp-=10
        else:
            self.player_hp-=10
        print(f"lost some tessure now the total tressre are {self.total_tressure} - Hp reduced {self.player_hp}")
        
    def battle(self): 
        k=random.randint(1,2)
        user_guess=input("guess if enemy is attacking or holding ! if attacking dodge else hold (dodge/hold):").lower()
        if k==1:
            print("enemy attacked ! dodge !!")
            if user_guess=='dodge' or user_guess=='d':
                print("nice dodge user gained some hp and saved alll the tressures")
            elif user_guess=='hold' or user_guess=='h':
                print("enemy attacked but user couldn't guess. user lost some tressures and lost some hp")
                self.total_tressure-=2
                self.player_hp-=10
                if self.player_hp>=1:
                    print(f"current tressures {self.total_tressure} and current hp {self.player_hp}")
                else:
                    print("user died !")
            else:
                print("wrong input")
            
        if k==2:
                print("enemy holded the attack ! you should hold the attack also !!")
                if user_guess=='hold' or user_guess=='h':
                    print("nice hold . user gained some hp and saved alll the tressures")
                    if self.player_hp<100:
                        self.player_hp+=5
                        print(f"current tressures {self.total_tressure} and current hp {self.player_hp}")
                    else:
                        print("nice hold . user saved alll the tressures")

                elif user_guess=='dodge' or user_guess=='d':
                    print("enemy holding attack but user dodged at wrong time and got hitten by enemy hold skill. user lost some tressures and lost some hp")
                    self.total_tressure-=2
                    self.player_hp-=10
                    if self.player_hp>=1:
                        print(f"current tressures {self.total_tressure} and current hp {self.player_hp}")
                    else:
                        print("user died !")
                else:
                    
                    print("wrong input")    
    
    def baited(self):
        self.player_hp-=10
        for _ in range(1,5):
            print("fall damaage !!!!! -2.5")
        print(f"current hp {self.player_hp}")
        print("user fell down in the hole ! now the user had to get out of the hole")
        
        print("USER SEES 4 WAYS IN THE HOLE1 ALL OF THEM LEADS OUT BUT ONLY ONE OF THEM IS SAFE !")

        Gates=random.randint(1,4)
        way=input("enter the way you wanna go ! remember only oone way is safe...........(north/south/east/west)(n/s/e/w)").lower()

        print(f"user choosed {way} now it depends if this way is safe or not")
        if Gates==1:
            if way=='east' or way=='e':
                print("This way was full of traps ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=5:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=5
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")
                    

            elif way=="north" or way=='n':
                print("This way had lots of enemies ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=10:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=10
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")

            elif way=="south" or way=="s":
                print("This way had some toxic gas ! user took damage but didnt lose any tressure")
                self.player_hp-=25
                print(f"user finally found the way out . current player {self.player_hp} but user does not had to lose his tressures {self.total_tressure}")
            else:
                print("only this way was safe West!!   GOOD DECISION ")
        
        if Gates==2:
            if way=='north' or way=='n':
                print("This way was full of traps ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=5:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=5
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")
                    

            elif way=="south" or way=='s':
                print("This way had lots of enemies ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=10:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=10
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")

            elif way=="west" or way=="w":
                print("This way had some toxic gas ! user took damage but didnt lose any tressure")
                self.player_hp-=25
                print(f"user finally found the way out . current player {self.player_hp} but user does not had to lose his tressures {self.total_tressure}")
            else:
                print("only this way was safe East!!   GOOD DECISION ")

        if Gates==3:
            if way=='south' or way=='s':
                print("This way was full of traps ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=5:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=5
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")
                    

            elif way=="west" or way=='w':
                print("This way had lots of enemies ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=10:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=10
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")

            elif way=="east" or way=="e":
                print("This way had some toxic gas ! user took damage but didnt lose any tressure")
                self.player_hp-=25
                print(f"user finally found the way out . current player {self.player_hp} but user does not had to lose his tressures {self.total_tressure}")
            else:
                print("only this way was safe North!!   GOOD DECISION ")

        if Gates==4:
            if way=='west' or way=='w':
                print("This way was full of traps ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=5:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=5
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")
                    

            elif way=="east" or way=='e':
                print("This way had lots of enemies ! user took so much damage and lost tons of its tressure")
                if self.total_tressure<=10:
                    self.player_hp-=25
                    self.total_tressure=0
                    print(f"user finally found the way out . current player {self.player_hp} and user had to give up on tressures {self.total_tressure}")
                else:
                    self.total_tressure-=10
                    self.player_hp-=25
                    print(f"user finally found the way out . current player {self.player_hp} and user had to lose tressures {self.total_tressure}")

            elif way=="north" or way=="n":
                print("This way had some toxic gas ! user took damage but didnt lose any tressure")
                self.player_hp-=25
                print(f"user finally found the way out . current player {self.player_hp} but user does not had to lose his tressures {self.total_tressure}")
            else:
                print("only this way was safe South!!   GOOD DECISION ")

            
        

    def randombox(self):
        while True:
            var=input("wanna go the te next step yes or no :")
            if var=='yes' or var=='y':
                i=random.randint(1,8)
                if i==1 or i==6 or i==8:
                    print("lucky got a tressure")
                    self.tres()
                elif i==3 or i==4:
                    print("there was a trap lost some of the tressure and lose some Hp")
                    
                    self.trap()
                elif i==2 or i==7:
                    print("there's a enemy! get ready for battle")
                    self.battle()
                elif i==5:
                    print("there was hole! ")
                    self.baited()
            else:
                print("the total numbers of tressure user was able to get is ",self.total_tressure)
                break

            if self.player_hp<=0:
                print("user died ! Game Over .")
                break

            if self.total_tressure<=0:
                self.total_tressure=0


            if self.total_tressure>=20:
                print(f"User Won the Game cureent tressures {self.total_tressure}")
                break



obj=The()


Try=input("Its a game of life and tresssures ! Only handful of guys can survive here (Yes or No):").lower()

if Try=="yes" or "y":
    print("Here We Go")
    obj.randombox()
    
else:
    print("okay get back when you are good enough")
    
        
