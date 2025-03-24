def main():
    bunny = Bunny()
    bunny.run()

if __name__ == "__main__":
    main()
    

class Prey:
    def run(self):
        print("HELP ME! I AM BEING CHASED!!")
    
class Predator:
    def chase(self):
        print("COME HERE, LIL' BRO! YOU CAN'T RUN AWAY FROM ME!!")
    
class Bunny(Prey):
    pass
    
class Tiger(Predator):
    pass
    
class Fish(Prey, Predator):
    pass
    

