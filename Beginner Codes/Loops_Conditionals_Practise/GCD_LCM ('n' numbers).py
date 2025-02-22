39
def main():
    # Take Input
    while True:
        try:
            mode = input("Do you want to find GCD or LCM or both? ").strip().upper()
            if mode == "BOTH":
                quantity = int(input(f"How many numbers do you want to find GCD/LCM of? "))
            elif mode == "GCD" or mode == "LCM" or mode == "HCF":
                quantity = int(input(f"How many numbers do you want to find {mode} of? "))
            else:
                print("Enter the correct mode of operation!!")
            break
        except ValueError:
            print("Enter only integeral numbers!!")
        
    numbers = []
    for i in range(1, quantity + 1):
        number = int(input(f"Enter number_{i}: "))
        numbers.append(number)
    
    # Print the result
    gcd = find_GCD(numbers)
    if mode == "GCD" or mode == "HCF":
        print(f"{mode} of the numbers is {gcd}")
    elif mode == "LCM":
        product = product_of_numbers(numbers)
        print(f"{mode} of the numbers is {int(product / gcd)}")
    else:
        product = product_of_numbers(numbers)
        print(f"GCD and LCM of the numbers are {gcd} and {int(product / gcd)} respectively.")
        

def find_GCD(numbers):
    
    # Find greatest number
    smallest_number = numbers[0]
    for number in numbers:
        if smallest_number > number:
            smallest_number = number 
    
    # Find divisors of the smallest number
    small_num_divisors = find_divisors(smallest_number)
    
    # Find and compare the divisors of other numbers
    divisors_count = {}
    for divisor in small_num_divisors:
        divisors_count[divisor] = 0  
    
    for number in numbers:
        if number != smallest_number:
            divisors = find_divisors(number)
            divisors.reverse()
            for divisor in divisors:
                if divisor in small_num_divisors:
                    divisors_count[divisor] += 1
                            
    # Find GCD
    gcd = max(divisors_count, key = divisors_count.get)
    # for divisor in small_num_divisors:
    #     if divisors_count.get(divisor) == max_value:
    #         gcd = divisor
    return gcd
        

def find_divisors(number):
    divisors = []
    for i in range(2, number // 2 + 1): # Double Slash -> integer division (floor division)
        if number % i == 0:
            divisors.append(i)
    return divisors

    
# Find product of numbers (Useful for finding LCM)
def product_of_numbers(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
    
    
if __name__ == "__main__":
    main()
    