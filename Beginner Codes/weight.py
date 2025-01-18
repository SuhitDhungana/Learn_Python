def main():
    weight = float(input("Enter the weight: "))
    type = input("What is the unit of weight (kg / lb)? ")
    
    if type == "kg":
        print(f"{weight}kgs is {weight * 2.2}pounds")
    elif type == "lb":
        print(f"{weight}pounds is {weight / 2.2}kgs")
main()