class Animal:
    def __init__(self, wake, eat, sleep):
        self.wake = wake
        self.eat = eat
        self.sleep = sleep
    
class Rat(Animal):
    def __init__(self, wake, eat, sleep, squeak):
        super().__init__(wake, eat, sleep)
        self.squeak = squeak

class Chimpanzee(Animal):
    def __init__(self, wake, eat, sleep, climb_tree):
        super().__init__(wake, eat, sleep)
        self.climb_tree = climb_tree

rat = Rat("6 AM", "bugs", "10 PM", "SQUEAKK")
print(f"A rat, who woke at {rat.wake} and ate {rat.eat} after shouting, '{rat.squeak},' slept at {rat.sleep}.")