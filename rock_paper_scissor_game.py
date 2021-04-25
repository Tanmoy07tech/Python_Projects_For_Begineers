import random

def play():
    print("### Welcome to Rock Paper Scissor Game ###")
    
    rounds=int(input("\n How many rounds you want to play? "))

    user_score=0
    computer_score=0

  

    for i in range(0,rounds,1):
        user=input("What's your chois? 'r' for rock , 'p' for paper ,'s' for scissors \n")
        computer=random.choice(['r','p','s'])
        if is_round_win(user,computer):
            print("You won this round")
            user_score=user_score+1
    
        elif is_round_win(user,computer)!=True:
            print("Computer won this round")
            computer_score=computer_score+1
        else:
            print("Its a tie round")

    print("Your Score is ",user_score)
    print("Computer Score is",computer_score)
    winner_decider(user_score,computer_score)
   


def is_round_win(player,opponent):
    #return true if player wins
    #r>s,s>p,p>r

    if (player=='r' and opponent =='s') or(player=='s' and opponent =='p') or (player=='p' and opponent =='r'):
        return True


def winner_decider(user_score,computer_score):
     if(user_score>computer_score):
        print("You won the game")
     elif(user_score<computer_score):
        print("Computer won the game \n Better luck next time")
     else:
        print("Scores are level..Game tied")

play()