def main():
    while True:
        alphabet_type = input("Do you want alphabet list to be in upper or lowercase (U / L)? ").strip().upper()
        
        if alphabet_type == "L":
            alphabet_list(97, 123)
            break
        elif alphabet_type == "U":
            alphabet_list(65, 91)
            break
        else:
            print("Enter L or U! No other alphanumeric character!")
    

def alphabet_list(start, end):
    for i in range(start, end):
        print(chr(i), end = " ")
        

if __name__ == "__main__":
    main()

        