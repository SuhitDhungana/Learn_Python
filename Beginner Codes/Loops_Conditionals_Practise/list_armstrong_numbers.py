def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter only numerical value!")
    
    list_armstrong_number(number + 1)
    

def list_armstrong_number(number):
    for i in range(1, number):
        temp = i
        sum = 0
        
        while temp != 0:
            last_digit = temp % 10
            sum += last_digit ** 3
            temp = (temp - last_digit) / 10
    
        if sum == i:
            print(i, end = " ")
        
        
if __name__ == "__main__":
    main()