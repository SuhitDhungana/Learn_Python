'''Pascal triangle's n'th row basically gives the binomial coefficient of terms 
i.e. for nth row, it gives coefficients of nC0, nC1, ...., nCn'''

def main():
    rows = int(input("Upto which row do you want the Pascal's triangle? "))
    spaces = rows - 1
    
    # Query for each Pascal Triangle's row
    for power in range(0, rows):
        # Space in beginning of each row
        for _ in range(spaces):
            print(" ", end = " ")
            
        # Calculate binomial coefficient
        r = 0
        while r <= power:
            coeff = int(bin_coeff(power, r))
            print(coeff, end = "   ")
            r += 1

        spaces -= 1
        print()
    
# Apply the formula nCr = n! / {(n-r)! * r!}
def bin_coeff(upperOfC, bottomOfC):
    n = factorial(upperOfC)
    r = factorial(bottomOfC)
    diff = factorial(upperOfC - bottomOfC)
    
    return n / (r * diff)

# Compute factorial
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    

if __name__ == "__main__":
    main()
            
    
            
            
            
        
        
        
