class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("This can drive")

    def parking(self):
        print("This needs some space for parking")