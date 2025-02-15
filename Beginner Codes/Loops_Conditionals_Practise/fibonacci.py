import math
def main():
    try:
        n = int(input("Till what term do you want the fibonacci series to run? "))
    except ValueError:
        print("Enter n'th term, not non-numeric character!")
    
    ''' Logic for fibonacci without recursion'''
    # a = 0
    # b = 1
    
    # for i in range(round(n / 2)):
    #     print(a, end = "  ")
    #     print(b, end = "  ")
    #     temp  = b
    #     a += b
    #     b += a
        
    

if __name__ == "__main__":
    main()
        
        