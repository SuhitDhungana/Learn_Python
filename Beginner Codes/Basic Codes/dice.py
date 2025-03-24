import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
def main():
    dice = {
        1: ("┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"),
        2: ("┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"),
        3: ("┌─────────┐",
            "│ ●       │",
            "│    ●    │",
            "│       ● │",
            "└─────────┘"),
        4: ("┌─────────┐",
            "│  ●    ● │",
            "│         │",
            "│  ●    ● │",
            "└─────────┘"),
        5: ("┌─────────┐",
            "│ ●     ● │",
            "│    ●    │",
            "│ ●     ● │ ",
            "└─────────┘"),
        6: ("┌─────────┐",
            "│ ●     ● │",
            "│ ●     ● │",
            "│ ●     ● │",
            "└─────────┘")
    }
    
    print("************WELCOME TO DICE GAME************")
    while True:
        try:
            n = int(input("Enter the number of die that you want to roll: "))
            break     
        except ValueError:
            print("Enter an integer! ")
    
    print(dice[1])
    temp = calc(dice, n)
    print_faces(temp[0], temp[1], dice)
    
    
    
def calc(dice, n):
    
    faces = []
    sum = 0
    for i in range(0, n):
        faces.append(random.randint(1, 6)) # assigning random value from 1 to 6
        sum += faces[i] 
    return (sum, faces)


def print_faces(sum, faces, dice):
    
    print("************YOUR DICE ROLLS************")
    for face in faces:
        print(face)
        for i in range(0, 5):
            print(dice[face][i]) # printing die's face
        print("------------------")
    print("***********************")
    print(f"Your total sum of the dice rolls was {sum}")
        
if __name__ == "__main__":
    main()