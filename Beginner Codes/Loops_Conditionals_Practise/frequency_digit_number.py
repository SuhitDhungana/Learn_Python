def main():
    while True:
        try:
            number = int(input("Enter the number: "))
            break
        except ValueError:
            print("Only enter numerical value!")

    frequency = find_frequency(number)
    
    for key, value in frequency.items():
        if value > 0:
            print(f"Number {key} is repeated {value} times")
    

def find_frequency(number):
    numbers = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
        0 : 0        
    }
    
    temp = number
    
    while (temp != 0):
        last_digit = temp % 10
        numbers[last_digit] += 1
        temp = (temp - last_digit) / 10
        
    return numbers
    
    
if __name__ == "__main__":
    main()
        