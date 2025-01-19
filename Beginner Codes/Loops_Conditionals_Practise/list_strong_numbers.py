def main():
    while True:
        try:
            number = int(input("Enter the number: "))
            break
        except ValueError:
            print("Only enter numerical value!")
    
    list_strong_numbers(number + 1)
    

def list_strong_numbers(number):
    for i in range(1, number):
        temp = i
        factorial_sum = 0
        
        while (temp != 0):
            last_digit = temp % 10
            factorial_sum += factorial(last_digit)
            temp = (temp - last_digit) / 10
            
        if factorial_sum == i:
            print(i, end = " ")
        
   
def factorial(number):
    if (number == 0 or number == 1):
        return 1
    else:
        return number * factorial(number - 1)    


if __name__ == "__main__":
    main()