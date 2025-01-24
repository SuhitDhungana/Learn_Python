def main():
    # Taking inputs
    decimal_number = int(input("Enter number in decimal number system (base 10): ").strip())
    system = input("In which number system do you want to change (Binary, Quinary, or Hexadecimal)? ").strip().lower()
    result = 0
    if system == "binary":
        result = convert_into_binary(decimal_number)
    elif system == "quinary":
        result = convert_into_quinary(decimal_number)
    elif system == "hexadecimal":
        result = convert_into_hexadecimal(decimal_number)
    else:
        print("Enter the correct number system where you'd like to convert!!")
        
    print(f"{decimal_number} converted in {system.title()} number system is {result}")


def convert_into_binary(decimal_number):
    binary_number_list = []
    while decimal_number != 0:
        remainder = decimal_number % 2
        binary_number_list.append(remainder)
        decimal_number = int(decimal_number / 2)
        
    binary_number_list.reverse()
    binary_number = ""
    
    for bin_number in binary_number_list:
        binary_number += str(bin_number)
    
    return binary_number


def convert_into_quinary(decimal_number):
    pass


def convert_into_hexadecimal(decimal_number):
    pass


if __name__ == "__main__":
    main()
        
        