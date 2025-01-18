def main():  
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter only numerical value!")
            
    if check_palindrome(number) == True:
        print(f"{number} is palindrome!")
    else:
        print(f"{number} isn't palindrome!")
        

def check_palindrome(number):
    temp = number
    power = 1
    reversed_number = 0
    
    # Find reversed number
    while temp != 0:
        last_digit = temp % 10
        reversed_number += last_digit * (10 ** power)
        power += 1
        temp = (temp - last_digit) / 10
    
    # Check if number is palindrome
    if reversed_number == number:
        return True
    else:
        return False    
    
    
if __name__ == "__main__":
    main()