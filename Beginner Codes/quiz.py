def main():
    """ I need to ask 5 question; give options to that question, have a specific 
        answer ready, take an answer from user, and tally a final score """
    
    questions = ("What is your name? ", 
                 "What is your birth month? ", 
                 "What is your favorite food? ",
                 "What is your dream university? ")
    
    options = (("Shaily", "Sita", "Suhit", "Hari"), 
               ("January", "February", "March", "April"),
               ("Brinjal", "Pizza", "Burger", "Bacon"),
               ("Harvard", "Sewanee", "UTA", "USM"))
    
    answers = ("Suhit", "January", "Burger", "Harvard")
    
    earned = 0
    
    for i in range(0, len(questions)):
        print(questions[i])
        print("Here are the options (type the whole answer, or use number to depict answer): ")
        print(options[i])
        guess = input().strip().title()
        if guess == answers[i] or guess == i + 1:
            print(f"Amazing! Your answer is correct! You earned {5 * (i + 1)} marks.")
            earned += 5 * (i + 1)
        else:
            print(f"Incorrect! You earn 0 points!")
    
    print(f"Bravo! You passed the test with {earned} points!")
main()
        
        
    
    
    