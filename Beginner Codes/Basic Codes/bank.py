def main():
    
    money = float(input("What's the amount in your bank account initially? "))
    print("***********WELCOME TO BANK***********")
    print("What do you want to do? ")
    print("**********************")
    print("1 -> Show balance")
    print("2 -> Deposit money")
    print("3 -> Withdraw money")
    print("**********************")
    
    while True:
        try:
            choice = int(input("Enter the choice (1 - 3): ")) 
            if 1 <= choice <= 3:
                break    
        except ValueError:
            print("Enter an integer from 1 to 3: ")
    
    match choice:
        case 1:
            show_balance(money)
        case 2:
            deposit(money)
        case 3: 
            withdraw(money)
            
                    
def show_balance(money):
    print(f"The amount in your bank account is {money:.2f}")
    

def deposit(money):
    dep = float(input("What is the amount that you want to deposit? "))
    money += dep
    show_balance(money)
    

def withdraw(money):
    draw = float(input("What is the amount that you want to withdraw? "))
    money -= draw
    show_balance(money)


if __name__ == "__main__":
    main()