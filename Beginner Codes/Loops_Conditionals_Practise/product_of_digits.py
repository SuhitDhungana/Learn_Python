def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter only numerical value!")
    
    product_digits(number)
    

def product_digits(number):
    temp = number
    product = 1
    
    while temp != 0:
        last_digit = temp % 10
        product *= last_digit
        temp = (temp - last_digit) / 10
    
    print(f"Product of digits is {int(product)}")
        
        
if __name__ == "__main__":
    main()