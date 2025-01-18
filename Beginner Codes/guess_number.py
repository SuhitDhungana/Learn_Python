import random

def main():
    while True: # until all conditions satisfied, keep looping
        try:
            first = int(input("From which number do you want to start guessing? "))
            last = int(input("Upto which number do you want to guess? "))
            n = int(input("Enter your guess: "))
            if check(first, last, n) == True:
                break
        except ValueError: # for non-integer values
            print("Re-enter only integer values!")
            
    guess(first, last, n)
    
    
def check(first, last, n):
    if not first <= n <= last: 
        print(f"Your guess must be within {first} & {last}")
    elif not first < n:
        print(f"{first} must be smaller than {n}")
    elif not last > n:
        print(f"{last} must be greater than {n}")
    else:
        return True
    return False
        
        
def guess(first, last, n):
    rand = random.randint(first, last)
    if n == rand:
        print(f"Your guess, {n}, was correct!")
    else:
        print(f"Your guess, {n}, was incorrect!")
        
main()