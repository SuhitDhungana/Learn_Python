def main():
    # Taking Input
    while True:
    mode = input("Do you want to find GCD or LCM or both? ").split().upper()
    if mode == BOTH:
        quantity = int(input(f"How many numbers do you want to find GCD/LCM of? "))
    else:
        quantity = int(input(f"How many numbers do you want to find {mode} of? "))
        
    numbers = []
    for i in range(1, quantity + 1):
        number = int(input("Enter number_{i}: "))
        numbers.append(number)
    
    GCD = find_GCD(numbers)
    if mode == "GCD" or mode == "HCF":
        print(f"{mode} of the numbers is {GCD}")
    elif mode == "LCM":
        product = product_of_numbers(numbers)
        print(f"{mode} of the numbers is {int(product / GCD)}")
    else:
        
        
        
def find_GCD(numbers):
    
        
''' My algorithm for this
i) find the smallest number among the numbers
ii) find divisors of smallest number and make a dictionary of those divisors are key values
iii) for every other number in 'numbers,' check individual divisors, and if the divisors 
    match with the divisors of smallest number's divisors, add a frequency
iv) in that dictionary, find the highest number which has value equal to 'quantity'
'''
    
    
    
    
if __name__ == "__main__":
    main()
    