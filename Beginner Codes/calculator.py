def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter the 2nd number: "))
    operation = input("Enter the arithmetic operation: ")
    
    match operation:
        case "+":
            print(f"{a} + {b} = {a + b}")
        case "-":
            print(f"{a} - {b} = {a - b}")
        case "*":
            print(f"{a} * {b} = {a * b}")
        case "/":
            print(f"{a} / {b} = {a / b}")
        case "%":
            print(f"{a} % {b} = {a % b}")
        case "^":
            print(f"{a} ^ {b} = {a ^ b}")
        case _:
            print("Enter the correct operation!!")
                
main()