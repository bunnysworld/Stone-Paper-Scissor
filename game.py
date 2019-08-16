import random

list=["stone","paper","scissor"]

chances=5
no_of_chances=0
computer_score=0
player_score=0

print(" WELCOME TO  STONE : PAPER : SCISSOR")
print(" CHOOSE ANY \tStone \tPaper \tscissor")

# STARTING OF WHILE LOOP

while no_of_chances<chances:
    player_inp=input(" Stone : Paper : Scissor")
    comp_inp=random.choice(list)

#      CHECKING CONDITIONS

    if player_inp == comp_inp:
        print(" 0 :  POINTS ASSIGNED TO EACH ")
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")

    elif player_inp == "stone" and comp_inp == "paper":
        print(f"YOUR GUESS IS : {player_inp} AND COMPUTER GUESS IS :{comp_inp}")
        print(" COMPUTER WINS 1 POINT")
        computer_score+=1
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")
    elif player_inp == "stone" and comp_inp == "scissor":
        print(f"YOUR GUESS IS : {player_inp} AND COMPUTER GUESS IS :{comp_inp}")
        print("PLAYER WINS 1 POINT")
        player_score+=1
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")
    elif player_inp == "paper" and comp_inp == "stone":
        print(f"YOUR GUESS IS : {player_inp} AND COMPUTER GUESS IS :{comp_inp}")
        print("PLAYER WINS 1 POINT")
        player_score+=1
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")
    elif player_inp == "paper" and comp_inp == "scissor":
        print(f"YOUR GUESS IS : {player_inp} AND COMPUTER GUESS IS :{comp_inp}")
        print("COMPUTER WINS 1 POINT")
        computer_score+=1
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")
    elif player_inp == "scissor" and comp_inp == "stone":
        print(f"YOUR GUESS IS : {player_inp} AND COMPUTER GUESS IS :{comp_inp}")
        print("COMPUTER WINS 1 POINT")
        computer_score+=1
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")
    else:
        print(f"YOUR GUESS IS : {player_inp} AND COMPUTER GUESS IS :{comp_inp}")
        print("PLAYER WINS 1 POINT")
        player_score+=1
        print(f"COMPUTER POINT IS : {computer_score} AND YOUR POINT IS : {player_score}")

    #   END OF CHECKING CONDITIONS
    no_of_chances+=1
    print(f" CHANCE LEFT  : {chances-no_of_chances}")


#   END OF WHILE LOOP

print(" ----------------- GAME OVER -----------------")

if player_score>computer_score:
    print(f"PLAYER WON !  POINTS : {player_score} , DIFFERENCE IN POINTS : {player_score-computer_score}")
elif computer_score>player_score:
    print(f"COMPUTER WON!  POINTS : {computer_score} , DIFFERENCE IN POINTS : {computer_score-player_score}")
else :
    print(f"MATCH DRAW COMPUTER SCORE : {computer_score}, PLAYER SCORE : {player_score}")
