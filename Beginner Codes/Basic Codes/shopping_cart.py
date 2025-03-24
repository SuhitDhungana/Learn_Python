def main():
    
    items = []
    prices = []
    total = 0
    
    while True:
        item = input("Enter the item: (Press Q to exit) ")
        if item.upper() == "Q":
            break
        price = float(input(f"Enter the price of {item}: "))
        items.append(item)
        prices.append(price)
    
    for i in range(0, len(items)):
        print(f"{items[i].title().strip():<10} {prices[i]:>} ")
        total += prices[i]
       
    print()
    print(f"The total price is ${total:.2f}") 
        
main()