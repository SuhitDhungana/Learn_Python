def main():
    n = int(input("Enter the number: "))
    x = sum(n)
    print(x)
     
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
    
    
if __name__ == "__main__":
    main()