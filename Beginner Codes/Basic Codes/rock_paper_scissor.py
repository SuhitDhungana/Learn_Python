import random

def main():
    outcomes = ("Rock", "Paper", "Scissors")
    rand = random.choices(outcomes) # generates random choice from 'outcomes't
    temp = rand[0] # converting the list 'rand' to string 'temp'
    while True:
        play = input("Rock, paper, or scissors? (press 'q' to quit)").lower().strip()
        if play == "rock":
            rock(temp)
        elif play == "paper":
            paper(temp)
        elif play == "scissors":
            scissors(temp)
        elif play == "q":
            break
        else:
            print(f"Enter correct choice from {outcomes}")

def rock(rand):
    if rand == "Paper":
        print(f"You lost against {rand}")
    elif rand == "Scissors":
        print(f"You won against {rand}")
    else:
        print("It is a TIE!")
        
def paper(rand):
    if rand == "Scissors":
        print(f"You lost against {rand}")
    elif rand == "Rock":
        print(f"You won against {rand}")
    else:
        print("It is a TIE!")
           
def scissors(rand):
    if rand == "Rock":
        print(f"You lost against {rand}")
    elif rand == "Paper":
        print(f"You won against {rand}")
    else:
        print("It is a TIE!")

if __name__ == "__main__":
    main()
    
            
        