def main():
#     n = int(input("Enter the nth term upto which you want the sum: " ))
#     sum = find_sum(n)
#     print(f"The sum of first {n} natural numbers is {sum}")
    

# def find_sum(n):
    
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n + find_sum(n - 1)

    n = int(input("Enter the number whose factorial you want to find: "))
    fact = factorial(n)
    print(f"{fact} is the factorial of {n}")
    
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
            
        
if __name__ == "__main__":
    main() 