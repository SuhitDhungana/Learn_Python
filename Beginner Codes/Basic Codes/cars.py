class Car:
    owner = "Suhit"
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
car1 = Car("Mustang", 2024, "Grey", True)
car2 = Car("Toyota", 2012, "Red", False)
print(f"Your order is a(n) {car1.color} {car1.model}")