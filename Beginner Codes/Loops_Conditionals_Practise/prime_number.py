def main():
    while True:
        try:
            number = int(input("Enter the number: "))
            break
        except ValueError:
            print("Enter a numeric value!")
    
    prime_numbers(number + 1)
    

def prime_numbers(number):
    
    # Handling exceptions of 2 (the only even prime number)
    if (number - 1) > 2:
        print("2", end = " ")
    elif (number - 1) == 2:
        print("2")
        return 1
    
    # Printing prime numbers
    
    # Query for each odd number until 'number'
    for i in range(3, number, 2):
        # Check 'i' is prime or composite
        check_prime 
        for j in range(3, i, 2):
            if i % j == 0:
                check_prime = False
                break
            
            if check_prime 
                print(i, end = " ")
            
    
if __name__ == "__main__":
    main()
    
    
'''
Logic Brainstorming
i) to save some time, i could skip the even numbers as they are always composite
ii) for any number 'a' between 1 and 'number,' check if any number, n, from 1 to int (a / 2),
    divides 'a.' If it does, it's composite else prime
'''
