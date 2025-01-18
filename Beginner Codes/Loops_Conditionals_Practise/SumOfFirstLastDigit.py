def main():
    while True:
        try:
            number = int(input("Enter the number: "))
            break
        except ValueError:
            print("Enter a numeric value!")
    
    sum_digits(number)
    

def sum_digits(number):
    temp = number
    counter = 0
    
    while number > 10:
        number /= 10
        counter += 1
    
    first = int(temp / (10 ** counter))
    last = temp % 10
    print(f"Sum of 1st and last digit is {first + last}")
    

if __name__ == "__main__":
    main()