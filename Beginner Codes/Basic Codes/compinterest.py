def main():
    p = 0
    t = 0
    r = 0
    while not (p > 0 and t > 0 and r > 0):
        p = float(input("Enter the amount: "))
        t = float(input("Enter the time period that amount is taken: "))
        r = float(input("Enter the rate of interest: "))
    a = p * (1 + r / 100) ** t
    i = a - p
    print(f"The interest is ${i:.2f}, and the final amount to be paid is ${a:.2f}")
    
main()