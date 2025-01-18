def main():
    while True:
        try:
            number = int(input("Enter the number whose digits who want to count: "))
            break
        except ValueError:
            print("Enter a numeric value!")
    
    count_digit(number)
    

def count_digit(number):
    temp = number
    counter = 0
    
    while number > 10:
        number /= 10
        counter += 1
    
    print(f"{temp} has {counter + 1} digits")
        
    
if __name__ == "__main__":
    main()