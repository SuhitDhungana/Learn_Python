def main():
    temperature = input("Enter the temperature (C or F): ")
    unit = temperature[-1: ]
    temp = float(temperature[0: -1].strip())
    
    if unit == "C":
        print(f"{temp}C = {9 / 5 * temp + 32}F")
    elif unit == "F":
        print(f"{temp}F = {5 / 9 * (temp - 32)}C`")
    else:
        print("Wrong unit of temperature; use C or F!")    
main()