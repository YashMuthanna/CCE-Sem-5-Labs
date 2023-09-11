class Vehicle:
    def __init__(self):
        self.ownerName = ""
        self.vid = 0
        self.manufacturer = ""

class Passenger(Vehicle):
    def __init__(self):
        super().__init__()
        self.num = 0

    @classmethod
    def enterDetails(cls):
        cls.ownerName = input("Enter owner name: ")
        cls.vid = int(input("Enter Vehicle ID: "))
        cls.manufacturer = input("Enter Manufacturer name: ")
        cls.num = int(input("Enter number of passengers: "))

    @classmethod
    def displayDetails(cls):
        print("Owner name: ", cls.ownerName)
        print("Vehicle ID: ", cls.vid)
        print("Manufacturer Name: ", cls.manufacturer)
        print("Number of Passengers: ", cls.num)

obj = Passenger()
obj.enterDetails()
print("Stored as object, Diplaying: \n")
obj.displayDetails()
