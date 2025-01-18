class Animals():
    alive = True
    
    
class Dog(Animals):
    def speak(self):
        print("WOOF!")
        
    
class Cat(Animals):
    def speak(self):
        print("MEOW!")
        

class Car:
    alive = False
    def speak(self):
        print("BEEP!")


def main():
    animals = (Dog(), Cat(), Car())
    for animal in animals:
        animal.speak()
        print(animal.alive)
        

if __name__ == "__main__":
    main()
    