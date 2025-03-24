import random
import time
def main():
    slot_items = ("🍒", "🙂", "🍎", "🍌", "🍑")
    first = random.choices(slot_items)
    second = random.choices(slot_items)
    third = random.choices(slot_items)
    print("*****************WELCOME TO THE CASINO*****************")
    print()
    money = float(input("What's the total amount of money that you've carried in the casino? "))
    while True:
        bet = float(input("What amount do you want to bet on slot machine? "))
        presentation(slot_items, first[0], second[0], third[0])
        new_money = check(first[0], second[0], third[0], money, bet)
        show_money(new_money)
        choice = input("Do you want to quit now? (Y/N) ").upper().strip()
        if choice == "Y" or choice == "YES":
            break
        print("*****************************")


def presentation(slot_items, first, second, third):
    print("----------SPINNING----------")
    time.sleep(3)
    print(f"{first} || {second} || {third}")
    print("-----------------------------")
   

def check(first, second, third, money, bet):
    
    if first == second == third:
        money += 20 * bet
        print(f"CONGRATULATIONS! You won ${20 * bet}")
    else:
        money -= 10 * bet
        print(f"ALAS! You lost {10 * bet}")
        
    return money
        

def show_money(money):
    if money > 0:
        print(f"After the gamble, you now have ${money}!")
    else:
        print(f"You owe the casino ${(-1) * money}!")
        
        
if __name__ == "__main__":
    main()
    