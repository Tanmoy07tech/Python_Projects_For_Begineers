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




guess(10)

