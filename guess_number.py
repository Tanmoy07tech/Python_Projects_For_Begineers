import random       #imported the random library

def guess(x):       
    random_number=random.randint(1, x)      #implemented the random library to generate a random number
    guess=0
    while(guess!=random_number):
        guess=int(input(f"Guess a number between 1 and {x}"))
        if(guess<random_number):
            print("Sorry, guess again. Too low")
        elif guess>random_number:
            print("Sorry,guess again. Too high")
    
    print("Yay congrats .You have guessesd the number",random_number,"Correctly")

def computer_guess(x):
    low=1
    high=x
    feedback=" "
    while feedback!='c':
        if low !=high:
            guess=random.randint(low,high)
        else:
            guess=low 
        feedback=input(f"Is it {guess} too (H) , too low (L) , or correct (C)??").lower()
        if(feedback=="h"):
            high=guess-1
        elif feedback=='l':
            low=guess+1
    
print("yay the computer guessed your ",guess,"correctly!")


guess(10)
computer_guess(100)

