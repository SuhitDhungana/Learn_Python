def main():
    menu = {"Pizza": 3.00,
            "Burger": 4.50,
            "Coca-Cola": 5.00,
            "Cheesecake": 1.25}
    
    show_menu(menu)
    foods = shopping(menu)
    bill(foods[0], foods[1], menu)
    
    
def show_menu(menu):
    print("------- MENU -------")
    for key, value in menu.items():
        print(f"{key:10}: {value:.2f}")
    print("---------------------")
        
def shopping(menu):
    cart = []
    total = 0
    print("What do you want to buy? (q to quit) ")
    while True:        
        food = input()
        if food.lower() == "q":
            break
        elif menu.get(food) == None:
            print(f"{food} isn't on the menu!! Enter correct food from the menu! ")
        else:
            total += menu.get(food)
            cart.append(food)
    
    print("---------------------")
    return [total, cart]

def bill(total, cart, menu):
    print("The final bill is: ")
    print("ITEM          PRICE")
    for food in cart:
        print(f"{food:13} ${menu.get(food):.2f}")
    print()
    print(f"Total amount: ${total:.2f}")

main()
