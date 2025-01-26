def main():
    # Taking inputs
    decimal_number = int(input("Enter number in decimal number system (base 10): ").strip())
    system = input("In which number system do you want to change (Binary, Hexadecimal)? ").strip().lower()
    result = 0
    if system == "binary" or system == "bin":
        result = convert_into_binary(decimal_number)
    elif system == "hexadecimal" or system == "hexa":
        result = convert_into_hexadecimal(decimal_number)
    else:
        print("Enter the correct number system where you'd like to convert!!")
        
    print(f"'{decimal_number}' converted in '{system.title()}' number system is '{result}'")


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


def convert_into_hexadecimal(decimal_number):
    hexadecimal_number_list = []
    while decimal_number != 0:
        remainder = decimal_number % 16
        if remainder <= 9:
            hexadecimal_number_list.append(remainder)
        else:
            hexadecimal_number_list.append(chr(55 + remainder))
        decimal_number = int(decimal_number / 16)
        
    hexadecimal_number_list.reverse()
    hexadecimal_number = ""
    
    for hex_number in hexadecimal_number_list:
        hexadecimal_number += str(hex_number)
    
    return hexadecimal_number


if __name__ == "__main__":
    main()
        
        