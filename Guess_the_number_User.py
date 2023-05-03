import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"Guess the number between 1 and {x}\n>"))
        if guess<random_number:
            print("Try Again! Your guess is too low")
        elif guess>random_number:
            print("Try Again! Your guess is too high")
    print(f"Yeh!!Your guess {random_number} is correct")
def guess_comp(x):
    low=1
    high=x
    feedback=""
    while feedback!="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high(H), too low(L), or correct(C)??").lower()
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
    print(f"Yah! Computer has guessed the number {guess},correctly")
guess_comp(10)

