def main():
    while True:
        try:
            number = int(input("Of which number do you want the multiplication table of? "))
            times = int(input("Upto what number do you want this multiplication table to go? "))
            break
        except ValueError:
            print("Enter only numbers!")
    
    # Multiplication Table
    for i in range(1, times + 1):
        print(f"{number} * {i} = {number * i}")
    
    
if __name__ == "__main__":
    main()
        
        