def main():
    while True:
        try:
            number = int(input("Upto which number do you want to see perfect number(s)? "))
            break
        except ValueError:
            print("Only numerical value!")
            
    check_perfect_number(number + 1)
    
    
def check_perfect_number(number):
    # Query for all numbers before 'number'
    for i in range(1, number):
        divisors_sum = 0
        end = int(i / 2) + 1
        # Find sum of divisors of 'i'
        for j in range(1, end):
            if i % j == 0:
                divisors_sum += j
        
        # If 'i' is perfect number
        if divisors_sum == i:
            print(i, end = " ")
            
        
if __name__ == "__main__":
    main()  
    

